import aiohttp
import asyncio
import time


async def fetch_page(session, url):
    page_start = time.time()
    async with session.get(url) as response:
        print(response.status, f'| Page took {time.time() - page_start}s')
        return response.status


async def get_multiple_pages(loop,*urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))

        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop=loop)


urls = ['https://google.com' for i in range(50)]

start = time.time()
loop.run_until_complete(get_multiple_pages(loop,*urls))  # gives us a coroutine object
print(f'All pages took {time.time() - start}s')