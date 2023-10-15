from app import books


def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating, reverse=True)[:10]
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


# sorting by two things
def print_best_cheap_books():
    # for the books with same rating sort by price
    best_cheap_books = sorted(books, key=lambda x: (x.rating * -1, x.price))[:10]
    for book in best_cheap_books:
        print(book)


print("Best Books\n")
print_best_books()
print("\nCheapest Books\n")
print_cheapest_books()
print("\nBest Cheap Books\n")
print_best_cheap_books()
