# ---- Do not change the code below ----
# User identity dictionary
user = {
    'id': 1,
    'name': 'jose',
    'role': 'admin'
}


# delete_database() function, DO NOT CHANGE
def delete_database():
    # perform deletion
    print('Database deleted!')


def check_permission(func):
    def wrapper():
        if user.get('role') == 'admin':
            return func()
        else:
            raise PermissionError

    return wrapper


# Use the check_permission() decorator and delete_database() function to create a secure_delete_database() function:

secure_delete_database = check_permission(delete_database)
secure_delete_database()
