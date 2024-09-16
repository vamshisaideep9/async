import asyncio

async def download_file(file_id):
    print(f"Starting download of file {file_id}")
    await asyncio.sleep(2)
    file_size = file_id  * 10
    print(f"finished download of file {file_id} with size {file_size} MB")
    return file_size

async def main():
    file_size1 = await download_file(1)
    file_size2 = await download_file(2)
    file_size3 = await download_file(3)
    total_size = file_size1 + file_size2 + file_size3
    print(f"Total downloaded size: {total_size} MB")


asyncio.run(main())