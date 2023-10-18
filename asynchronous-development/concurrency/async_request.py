import aiohttp
import asyncio
import time


async def fetch_page(url):
    # suspend and resume context manager
    page_start = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(response.status, f'| Page took {time.time() - page_start}s')
            return response.status


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop=loop)


tasks = [fetch_page('https://google.com') for i in range(50)]

start = time.time()
loop.run_until_complete(asyncio.gather(*tasks))  # gives us a coroutine object
print(f'All pages took {time.time() - start}s')

