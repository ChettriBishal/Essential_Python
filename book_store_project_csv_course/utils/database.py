"""
Concerned with storing and retrieving books from a list
CSV File
name,author,read
"""

book_file = 'data.txt'


def add_book(name, author):
    # using files
    with open(book_file, 'a') as file:
        file.write(f'{name},{author},0\n')


def get_all_books():
    with open(book_file, 'r') as file:
        books = [book.strip().split(',') for book in file.readlines()]

        books = [
            {"name": book[0], "author": book[1], "read": book[2]}
            for book in books
        ]

    return books


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'

    _save_all_books(books)


def _save_all_books(books):
    with open(book_file, "w") as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
