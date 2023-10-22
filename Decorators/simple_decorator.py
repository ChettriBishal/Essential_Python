user = {'username': 'jose123', 'access_level': 'admin'}


# decorator which takes a function as a parameter and returns another function
def user_has_permission(func):
    if user.get('access_level') == 'admin':
        return func
    raise RuntimeError


def user_has_permission2(func):
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()

    return secure_func


def my_function():
    return 'Password for admin panel is 1234'


my_secure_function = user_has_permission2(my_function)

print(my_secure_function())
