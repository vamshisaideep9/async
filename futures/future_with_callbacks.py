#You can attach a callback to a future using the add_done_callback() method. 
# This is useful when you want to perform an action after the result of the future is available.

import asyncio

def future_callback(future):
    print(f"Call back: Future result is {future.result()}")


async def future_with_callback():
    future = asyncio.Future()

    future.add_done_callback(future_callback)

    await asyncio.sleep(2)

    future.set_result("Result with callback")


asyncio.run(future_with_callback())