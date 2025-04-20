from temporalio.worker import Worker
from workflows.dynamic_workflow import DynamicAPIWorkflow
from activities.api_runner import run_api_step

import asyncio

async def main():
    from temporalio.client import Client
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="yaml-workflows",
        workflows=[DynamicAPIWorkflow],
        activities=[run_api_step]
    )

    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
