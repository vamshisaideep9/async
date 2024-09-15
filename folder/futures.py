import asyncio

#A function to simulate a asynchronous operation using a future
async def async_operation(future, data):
    await asyncio.sleep(1) #simulate some async work with a delay

    if data == "success":
        future.set_result("Operation succeeded")
    else:
        future.set_exception(RuntimeError("Operation failed"))


#A callback function to be called when the future is done

def future_callback(future):
    try:
        print("callback: ", future.result())
    except Exception as exc:
        print("callback: ", exc)

async def main():
    future = asyncio.Future()

    #Add a callback to the future
    future.add_done_callback(future_callback)

    #Start async operation and pass the future
    await async_operation(future, "success")

    #Check if future is done and print its result
    if future.done():
        try:
            print("Main: ", future.result())
        except Exception as exc:
            print("Main: ", exc)

asyncio.run(main())