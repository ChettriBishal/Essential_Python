import logging
from app import books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Enter one of the following

- 'b' to look at 5-star books
- 'c' to look at the cheapest books
- 'n' to just get the next available book on the page
- 'q' to exit

Enter your choice: '''


def print_best_books():
    logger.info('Finding best books by rating...')
    best_books = sorted(books, key=lambda x: x.rating, reverse=True)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding cheapest books...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


# sorting by two things
def print_best_cheap_books():
    logger.info('Finding best cheap books...')
    # for the books with same rating sort by price
    best_cheap_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_cheap_books:
        print(book)


def print_five_star_books():
    logger.info('Finding five star books...')
    five_star_books = filter(lambda x: x.rating == 5, books)
    for book in five_star_books:
        print(book)


books_available = (x for x in books)  # generator


def print_next_available_book():
    logger.info('Getting the next book from the catalogue...')
    print(next(books_available))


user_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': print_next_available_book
}


def menu():
    choice = input(USER_CHOICE)
    while choice != 'q':
        if choice in ('b', 'c', 'n'):
            user_choices[choice]()
        else:
            print("Enter a valid choice!")

        choice = input(USER_CHOICE)

    logger.debug('Terminating the program...')


menu()
