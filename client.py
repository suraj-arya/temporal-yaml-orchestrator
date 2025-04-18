import asyncio
from temporalio.client import Client

async def main():
    with open("templates/sample_workflow.yaml") as f:
        yaml_def = f.read()

    client = await Client.connect("localhost:7233")

    result = await client.start_workflow(
        "DynamicAPIWorkflow",
        id="demo-workflow-001",
        task_queue="yaml-workflows",
        args=[yaml_def, {"userId": 1}])

    print(f"Started: {result}")

if __name__ == "__main__":
    asyncio.run(main())
