#asyncio.ensure_future() schedules a coroutine for execution and returns a future representing the eventual result.

import asyncio

async def coro_function():
    await asyncio.sleep(1)
    print("Coroutine completed")
    return "Result from coro_function"

async def main():
    future = asyncio.ensure_future(coro_function())
    print(f"Future scheduled: {future}")

    result = await future
    print(f"future result: {result}")

asyncio.run(main())

#asyncio.ensure_future(coro_function()): Schedules the coroutine to run and returns a future.
#The future will hold the result of the coroutine once it is finished.