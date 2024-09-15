import asyncio

async def task1():
    await asyncio.sleep(2)
    return "Task 1 complete"

async def task2():
    await asyncio.sleep(1)
    return "Task 2 complete"

async def main():
    future1 = asyncio.ensure_future(task1())
    future2 = asyncio.ensure_future(task2())

    results = await asyncio.gather(future1, future2)
    print(results)

asyncio.run(main())


#asyncio.gather(future1, future2): Runs both futures concurrently and collects their results.
#Task 2 will complete first, but gather() waits for both tasks before returning results.