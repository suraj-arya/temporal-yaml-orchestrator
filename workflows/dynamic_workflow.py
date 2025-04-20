import yaml
from temporalio import workflow
from datetime import timedelta

# Mark imports as pass through to allow them in the workflow sandbox
workflow.pass_through_imports = [
    "yaml",
    "jsonpath_ng",
    "aiohttp",
    "json",
    "jinja2"
]

@workflow.defn(sandboxed=False)
class DynamicAPIWorkflow:
    @workflow.run
    async def run(self, yaml_string: str, input_data: dict):
        try:
            from activities.api_runner import run_api_step
            doc = yaml.safe_load(yaml_string)
            context = {"input": input_data}

            for step in doc["steps"]:
                workflow.logger.info(f"Executing step: {step['name']}")
                workflow.logger.debug(f"Step details: {step}")
                workflow.logger.debug(f"Current context: {context}")
                result = await workflow.execute_activity(
                    run_api_step,
                    args=[step, context],
                    schedule_to_close_timeout=timedelta(seconds=60)
                )
                context[step["name"]] = result

            return context
        except Exception as e:
            # Simple error handling without complex logging
            raise Exception(f"Workflow failed: {str(e)}")
