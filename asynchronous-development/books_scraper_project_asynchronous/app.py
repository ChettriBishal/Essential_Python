import requests
import logging
import time
import aiohttp
import async_timeout
import asyncio

from pages.all_books_page import AllBooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')

logger = logging.getLogger('scraping')
logger.info('Loading books list...')

logger.info('Requesting http://books.toscrape.com')
page_content = requests.get('https://books.toscrape.com/').content

logger.debug('Creating AllBooksPage from page content.')
page = AllBooksPage(page_content)

books = page.books
# print(type(books))


# getting content from 50 pages
logger.info(f'Going through {page.page_count} pages of books...')

_books = []

start = time.time()


async def fetch_page(session, url):
    page_start = time.time()
    # if the session takes longer than 10s it's going to cancel the operation and an exception will be raised
    # async with async_timeout.timeout(10):
    logger.info(f'Requesting {url}')
    async with session.get(url) as response:
        print(response.status, f'| Page took {time.time() - page_start}s')
        return await response.text()


async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))

        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks  # program won't finish until all tasks have given you something


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop=loop)


logger.info(f'Going through {page.page_count} pages of books...')


urls = [f'http://books.toscrape.com/catalogue/page-{page_num + 1}.html' for page_num in range(page.page_count)]
start = time.time()

pages = loop.run_until_complete(get_multiple_pages(loop, *urls))

print(f'Total took {time.time() - start}')

for page_content in pages:
    logger.debug('Creating AllBooksPage from page content')
    page = AllBooksPage(page_content)
    _books.extend(page.books)

books = _books

