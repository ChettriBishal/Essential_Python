# import requests
# we don't need requests anymore as webdriver would be doing it

from selenium import webdriver

from pages.quotes_page import QuotesPage, InvalidTagForAuthorError

try:
    chrome = webdriver.Chrome()
    chrome.get('https://quotes.toscrape.com/search.aspx')
    page = QuotesPage(chrome)

    author = input("Enter the author whose quotes you'd like: ")
    # page.select_author(author)

    # tags = page.get_available_tags()
    # print("Select one of these tags: [{}]".format(" | ".join(tags)))
    tag = input("Enter your tag: ")
    # page.select_tag(tag)

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print("An unknown error occurred. Please try again.")

# page.search_button.click()
# print(page.quotes)
