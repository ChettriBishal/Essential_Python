"""
here we will be using a database
[
    {
        'name': 'Permanent Record',
        'author': 'Robert',
        'read': True
    }
    {

    }
]
list of dictionaries
Make sure the data.json file is not empty
should have [] in the beginning

"""

import json

book_file = 'data.json'


def create_empty_file():
    with open(book_file, 'w') as file:
        json.dump([], file)


def add_book(name, author):
    # using files
    books = get_all_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


def get_all_books():
    with open(book_file, 'r') as file:
        books = json.load(file)

    return books


def _save_all_books(books):
    with open(book_file, "w") as file:
        json.dump(books, file)


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = True

    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)
