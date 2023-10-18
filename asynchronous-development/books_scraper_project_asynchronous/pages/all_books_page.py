import re
import logging

from locators.all_books_page import AllBooksPageLocators
from parsers.book_parser import BookParser
from bs4 import BeautifulSoup

logger = logging.getLogger('scraping.all_books_page')  # child logger of the base logger


class AllBooksPage:
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{AllBooksPageLocators.BOOKS}`')
        return [BookParser(e) for e in self.soup.select(AllBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        logger.debug('Finding all number of catalogue pages available...')
        content = self.soup.select_one(AllBooksPageLocators.PAGER).string  # page 1 of 50

        logger.info(f'Found number of catalogue pages available: `{content}`')
        pattern = "Page [0-9]+ of ([0-9]+)"
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))

        logger.info(f'Extracted number of pages as integer: `{pages}`.')
        # print(f'Pages = {pages}')
        return pages
