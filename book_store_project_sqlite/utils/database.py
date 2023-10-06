"""
here we will be using a database sqlite
"""

import sqlite3

from .database_connection import DatabaseConnection

from typing import List, Dict, Union

Book = Dict[str, Union[str, int]]  # creating our own types

book_db = 'data.db'


def create_book_table() -> None:
    with DatabaseConnection(book_db) as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books (name text primary key,author text,read integer)')


'''
def add_book(name, author):
    connection = sqlite3.connect(book_db)
    cursor = connection.cursor()

    # command = f'INSERT INTO books(name,author,read) VALUES("{name}", "{author}",0)'
    # cursor.execute(command)

    # If a user tries to enter a value which is already present
    try:
        cursor.execute('INSERT INTO books VALUES(?,?,0)', (name, author))
        connection.commit()
    except sqlite3.IntegrityError as e:
        print(e)
    finally:
        connection.close()

'''


def add_book(name: str, author: str) -> None:
    with DatabaseConnection(book_db) as connection:
        cursor = connection.cursor()
        # cursor.execute('INSERT INTO books VALUES(?,?,0)', (name, author))
        try:
            cursor.execute('INSERT INTO books VALUES(?,?,0)', (name, author))
        except sqlite3.IntegrityError as e:
            print(e)


def get_all_books() -> List[Book]:
    with DatabaseConnection(book_db) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT* FROM books;')

        # fetchall() -> list of tuples, every tuple -> row

        books = cursor.fetchall()  # fetch all rows
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in books]

        # connection.close()
        # there's no need to commit in this case

    return books


def mark_book_as_read(name: str) -> None:
    # use update command
    try:
        if not _check_if_present(name):
            raise DoesNotExist(f'Record with book name {name} does not exist')
    except DoesNotExist as e:
        print(f'Error: {e}')
    else:
        with DatabaseConnection(book_db) as connection:
            cursor = connection.cursor()
            cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))


def delete_book(name: str) -> None:
    try:
        if not _check_if_present(name):
            raise DoesNotExist(f'Record with book name {name} does not exist')
    except DoesNotExist as e:
        print(f'Error: {e}')
    else:
        with DatabaseConnection(book_db) as connection:
            cursor = connection.cursor()

        cursor.execute('DELETE FROM books where name=?', (name,))


def _check_if_present(name: str) -> bool:
    with DatabaseConnection(book_db) as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books where name=?', (name,))
        check = cursor.fetchone()

    if check:
        return True
    return False


class DoesNotExist(Exception):
    pass
