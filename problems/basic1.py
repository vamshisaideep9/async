import asyncio

async def download_file(file_id):
    print(f"Starting download of file {file_id}")
    await asyncio.sleep(2)
    print(f"finished download of file {file_id}")

async def main():
    await download_file(1)
    await download_file(2)
    await download_file(3)


asyncio.run(main())