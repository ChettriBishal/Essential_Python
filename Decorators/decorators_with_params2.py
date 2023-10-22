import functools

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(panel):  # this function inherits everything from the original func in a way
        if user.get('access_level') == 'admin':
            return func(panel)

    return secure_func


@user_has_permission  # this decorator will work for `my_function` but won't work for another which doesn't have
# parameter
def my_function(panel):
    """
    my_function's docstring here
    """
    return f'Password for {panel} panel is 1234'


# my_secure_function = user_has_permission(my_function)

print(my_function("movies"))
