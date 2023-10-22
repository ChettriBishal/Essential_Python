# third level function params
# what if other users wanted to access it -> Making the parameter more generic

import functools

user = {'username': 'jose123', 'access_level': 'admin'}


def third_level(access_level):
    def user_has_permission(func):
        @functools.wraps(func)
        def secure_func(panel):  # this function inherits everything from the original func in a way
            if user.get('access_level') == access_level:
                return func(panel) # the innermost return is the function passed into parameter

        return secure_func

    return user_has_permission # the outer function that is defined is returned at the end


@third_level('admin')
# parameter
def my_function(panel):
    """
    my_function's docstring here
    """
    return f'Password for {panel} panel is 1234'


#
# my_function = third_level('admin')(my_function)
# print(my_function('movies'))

print(my_function('movies'))
