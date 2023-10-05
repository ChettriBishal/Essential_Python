"""
Concerned with storing and retrieving books from a list
This database will use lists to store the data
In Memory Database
"""


class Book:
    def __init__(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.read = False

    def show_book_details(self):
        read = 'Yes' if self.read else 'No'
        print(f'{self.book_name} by {self.author}, read: {read}')


class Books:

    def __init__(self, books=None):
        if books is None:
            books = []
        elif books is not None:
            self.books = books
        else:
            self.books = []
        self.books = []
        self.books_cnt = len(books)

    def add_book(self):
        book_name, author = input("Enter the book name and author separated by commas: ").split(',')
        my_book = Book(book_name, author)
        print(book_name, author)
        self.books.append(my_book)
        print(f'{book_name} successfully added to your list')

    def mark_book(self):
        book_name = input("Enter the book you want to mark as read: ")
        for book in self.books:
            if book.book_name.lower() == book_name.lower():
                book.read = True
                break
        print(f'{book_name} marked as read successfully')

    @property
    def total_books(self):
        return len(self.books)

    def delete_book(self):
        book_to_delete = input("Enter the name of the book to delete: ")

        for i in range(len(self.books)):
            if self.books[i].book_name.lower() == book_to_delete.lower():
                # means we found the book
                self.books_cnt -= 1
                print(f'{self.books[i].book_name} successfully removed!')
                del self.books[i]
                break

    def list_books(self):
        print(f'Total number of books = {self.total_books}')
        for book in self.books:
            book.show_book_details()
            print('\n')
