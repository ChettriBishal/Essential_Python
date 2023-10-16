import requests
from bs4 import BeautifulSoup

'''
html_content = requests.get("https://books.toscrape.com/").content

NAME_LOCATOR = 'article.product_pod h3 a'

soup = BeautifulSoup(html_content,'html.parser')
locator = soup.select_one(NAME_LOCATOR)

print(locator.attrs['title'])
'''

html_content = requests.get('https://quotes.toscrape.com/').content

QUOTE_LOCATOR = 'div.quote'

soup = BeautifulSoup(html_content,'html.parser')

locator = soup.select(QUOTE_LOCATOR)

for loc in locator:
    print(loc.content)
print(locator)

