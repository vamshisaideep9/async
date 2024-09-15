import asyncio

async def simple_future():
    future = asyncio.Future()

    await asyncio.sleep(1)

    future.set_result('future result')

    print(f"Future result: {await future}")

asyncio.run(simple_future())


#comments
#asyncio.Future(): Creates a future object.
#future.set_result('Future Result'): After the asynchronous operation, the result is set.
#await future: Retrieves the result when it becomes available.