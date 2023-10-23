"""
Creating a decorator class
"""


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper function executed before {original_function.__name__}")

        return original_function(*args, **kwargs)

    return wrapper_function


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    # this acts like the wrapper for original function
    def __call__(self, *args, **kwargs):
        print(f"call method function executed before {self.original_function.__name__}")

        return self.original_function(*args, **kwargs)


# display = decorator_function(display) -> equivalent to what's below (17 - 18)
@decorator_class
def display():
    print('Display function ran')


@decorator_class
def display_info(name, age):
    print(f"display_info ran with arguments ({name},{age})")


display_info('Bishal', '21')

display()
