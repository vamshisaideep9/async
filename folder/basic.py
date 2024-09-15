#THis is synchronization method
# import time

# def say_hello():
#     time.sleep(2)
#     print("Hello, Async wold? (Not yet)")
# say_hello()


#This is Asynchronization method

import asyncio

async def say_hello_async():
    await asyncio.sleep(2) #simulates waiting for 2 seconds
    print("Hello, Async world!")

async def do_something_else():
    print("Starting another task...")
    await asyncio.sleep(1) #Simulates doing something else for 1 second
    print("Finished another task")

async def main():

    #Schedule both tasks to run concurrently
    await asyncio.gather(
        say_hello_async(),
        do_something_else(),
    )

asyncio.run(main())


