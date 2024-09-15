#Synchronous reading multiple files
import time
# start_time = time.time()
# print(start_time)
# def read_file_sync(filepath):
#     with open(filepath, 'r') as file:
#         return file.read()
    
# def read_all_sync(filepaths):
#     return [read_file_sync(filepath) for filepath in filepaths]


# filepaths = ['file1.txt','file2.txt']
# data = read_all_sync(filepaths)
# print(start_time - time.time())
# print(data)

#For asynchronous version

import aiofiles
import asyncio

start_time = time.time()
print(start_time)

async def read_file_async(filepath):
    async with aiofiles.open(filepath, 'r') as file:
        return await file.read()

async def read_all_async(filepaths):
    tasks = [read_file_async(filepath) for filepath in filepaths]
    return await asyncio.gather(*tasks)

async def main():
    filepaths = ['file1.txt', 'file2.txt']
    data = await read_all_async(filepaths)
    print(data)



asyncio.run(main())

print(start_time - time.time())
