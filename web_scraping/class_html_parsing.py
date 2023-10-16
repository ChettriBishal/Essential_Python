import re

from bs4 import BeautifulSoup

ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
            <p class="star-rating Three">
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
                <i class="icon-star"></i>
            </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>

</body></html>
'''


class ParsedItem:
    """
    A class to take in HTML page or content,and find properties of an item
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = 'article.product_pod h3 a'
        item_link = self.soup.select_one(locator)  # selects the first one which matches the locator pattern
        item_name = item_link.attrs['title']
        return item_name

    @property
    def link(self):
        locator = 'article.product_pod h3 a'
        item_link = self.soup.select_one(locator)
        link = item_link.attrs['href']
        return link

    @property
    def price(self):
        locator = 'article.product_pod p.price_color'
        item_price = self.soup.select_one(locator)
        # item_price = float(item_price.string[1:])  # removing the pound sign

        # using regex
        pattern = r"£([\d]+.?[\d]*)"
        pattern2 = r"£([0-9]+\.[0-9]+)"
        item_price = re.search(pattern, item_price.string)
        # print(item_price.group(0))
        # print(item_price.group(1))
        return item_price.group(1)

    @property
    def rating(self):
        locator = 'article.product_pod p.star-rating'
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']
        print(classes)
        classes = filter(lambda x: x != 'star-rating', classes)
        # classes = [r for r in classes if r!= 'star-rating']
        # print(classes)
        # print(next(classes))
        return next(classes)


item = ParsedItem(ITEM_HTML)
print(item.name)
print(item.price)
print(item.rating)
print(item.link)
