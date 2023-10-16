from bs4 import BeautifulSoup
from locators.books_page_locator import BooksPageLocator
from parsers.book import BookParser


class BooksPage:
    def __init__(self, html_page):
        self.soup = BeautifulSoup(html_page, 'html.parser')

    @property
    def books(self):
        locator = BooksPageLocator.BOOKS
        book_tags = self.soup.select(locator)
        return [BookParser(b) for b in book_tags]
