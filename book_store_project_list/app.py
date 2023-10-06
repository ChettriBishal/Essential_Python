import utils.database

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
    user_collection = utils.database.Books()

    while user_input != 'q':
        if user_input == 'a':
            user_collection.add_book()
        elif user_input == 'l':
            user_collection.list_books()
        elif user_input == 'r':
            user_collection.mark_book()
        elif user_input == 'd':
            user_collection.delete_book()
        elif user_input == 'q':
            break

        user_input = input(USER_CHOICE)


if __name__ == "__main__":
    menu()
