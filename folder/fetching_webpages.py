#This is synchronous version
# import requests
# import time

# start_time = time.time()

# def fetch_url(url):
#     return requests.get(url).text



# page1 = fetch_url('http://example.com')
# page2 = fetch_url('http://example.org')

# print(f"Done in {time.time() - start_time} seconds")


#Asynchronous version

import aiohttp
import asyncio
import time


async def fetch_async(url,session):
    async with session.get(url) as response:
        return await response.text()
    

async def main():
    async with aiohttp.ClientSession() as session:
        page1 = asyncio.create_task(fetch_async('http://example.org', session))
        page2 = asyncio.create_task(fetch_async('http://example.org',session))
        await asyncio.gather(page1, page2)

start_time = time.time()
asyncio.run(main())
print(f"Done in {time.time() - start_time} seconds")



