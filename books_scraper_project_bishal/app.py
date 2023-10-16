from pages.books_page import BooksPage
import requests


url = 'https://books.toscrape.com/'
page_content = requests.get(url).content
response = page_content
book_collection = BooksPage(response).books

print('BOOKS')
for book in book_collection:
    print(book)
