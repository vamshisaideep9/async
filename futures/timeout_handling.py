import asyncio

async def slow_task():
    await asyncio.sleep(5)
    return "Slow task completed"


async def main():
    try:
        result = await asyncio.wait_for(slow_task(), timeout=2)
        print(result)
    except asyncio.TimeoutError:
        print("The task took too long it was cancelled")


asyncio.run(main())

#asyncio.wait_for(slow_task(), timeout=2): Sets a timeout of 2 seconds for the slow task.
#If the task takes longer than the timeout, a TimeoutError is raised, and the task is canceled.