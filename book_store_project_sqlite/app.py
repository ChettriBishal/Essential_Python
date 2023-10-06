import utils.database as db

USER_CHOICE = """
************
BOOK STORE 
************

Enter: 
a: To add a new book 
l: To list all books 
r: To mark a book as read
d: To delete a book
q: To quit 

Your Choice: """


def menu():
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_remove_book()
        elif user_input == 'q':
            pass

        user_input = input(USER_CHOICE)


def prompt_add_book():
    name, author = input("Enter the name of the book and author separated by comma: ").split(',')
    db.add_book(name, author)


def list_books():
    books = db.get_all_books()
    for book in books:
        # print(book)
        read = 'Yes' if book['read'] else 'No'
        print(f'{book['name']} by {book['author']}: read {read}')


def prompt_read_book():
    name = input("Enter the name of the book you finished reading: ")
    db.mark_book_as_read(name)


def prompt_remove_book():
    name = input("Enter the name of the book to delete: ")
    db.delete_book(name)


if __name__ == "__main__":
    db.create_book_table()
    menu()
