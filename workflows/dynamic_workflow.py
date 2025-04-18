import yaml
from temporalio import workflow


@workflow.defn
class DynamicAPIWorkflow:
    @workflow.run
    async def run(self, yaml_string: str, input_data: dict):
        from activities.api_runner import run_api_step
        doc = yaml.safe_load(yaml_string)
        context = {"input": input_data}

        for step in doc["steps"]:
            print(f"running step: {step}")
            result = await workflow.execute_activity(
                run_api_step,
                step,
                context,
                schedule_to_close_timeout=60
            )
            context[step["name"]] = result
