"""
Concerned with storing and retrieving books from a list
This database will use lists to store the data
In Memory Database
"""


class Book:
    def __init__(self, book_name, author, read=False):
        self.book_name = book_name
        self.author = author
        self.read = read

    def show_book_details(self):
        read = 'Yes' if self.read else 'No'
        print(f'{self.book_name} by {self.author}, read: {read}')


class Books:
    def __init__(self, books_cnt=None):
        with open('data.txt', 'r') as file:
            book_list = file.readlines()

        self.books_cnt = len(book_list)

    @staticmethod
    def add_book():
        book_name, author = input("Enter the book name and author separated by commas: ").split(',')

        with open('data.txt', 'a') as file:
            file.write(f"'{book_name.title()}','{author.title()}',{False}\n")

        print(f'{book_name} successfully added to your list')

    @staticmethod
    def mark_book():
        book_name = input("Enter the book you want to mark as read: ")

        with open('data.txt', 'r') as file:
            books_info = file.readlines()
            updated_info = []
            for book in books_info:
                name, author, read = book.split(',')
                name = name.replace("'", '')  # remove the trailing ''
                if name.lower() == book_name.lower():
                    updated_info.append(f"'{name.title()},{author},{True}\n")
                else:
                    updated_info.append(book)

        with open('data.txt', 'w') as file:
            file.writelines(updated_info)  # overwriting the previous file with this

        print(f'{book_name} marked as read!!')

    @property
    def total_books(self):
        return self.books_cnt

    @staticmethod
    def delete_book():
        book_to_delete = input("Enter the name of the book to delete: ")
        with open('data.txt', 'r+') as file:
            books_info = file.readlines()
            updated_info = []
            for book in books_info:
                name, author, read = book.split(',')
                name = name.replace("'", '')
                if name.lower() != book_to_delete.lower():
                    updated_info.append(book)

        with open('data.txt', 'w') as file:
            file.writelines(updated_info)

        print(f'{book_to_delete} removed successfully!!')

    @staticmethod
    def list_books():
        with open('data.txt', 'r') as file:
            book_list = file.readlines()
            for book in book_list:
                name, author, read = book.split(',')
                read = read.strip()
                read = 'Yes' if read == 'True' else 'No'
                print(f'{name} by {author}: read: {read}')
