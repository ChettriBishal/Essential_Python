from locators.books_locator import BooksLocator


class BookParser:
    """
    Given one parent book id, find its name, price and rating
    """

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f"""
        Name: {self.name}
        Price: {self.price}
        Link: {self.link}
        Rating: {self.rating}
"""

    @property
    def name(self):
        locator = BooksLocator.NAME
        name_tag = self.parent.select_one(locator)
        book_name = name_tag.attrs['title']
        return book_name

    @property
    def link(self):
        locator = BooksLocator.LINK
        link_tag = self.parent.select_one(locator)
        book_link = link_tag.attrs['href']
        return book_link

    @property
    def price(self):
        locator = BooksLocator.PRICE
        return self.parent.select_one(locator).string

    @property
    def rating(self):
        locator = BooksLocator.RATING

        # select only the rating
        star_rating_tag = self.parent.select_one(locator)

        classes = star_rating_tag.attrs['class']
        required_rating = filter(lambda x: x != 'star-rating', classes)
        return next(required_rating)
