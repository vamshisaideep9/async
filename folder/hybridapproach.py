import asyncio
import time


def sync_task():
    print("Starting a slow sync task ...")
    time.sleep(5)
    print("Finished the slow task.")


async def async_wrapper():
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, sync_task)


async def main():
    await asyncio.gather(
        async_wrapper()
    )

asyncio.run(main())