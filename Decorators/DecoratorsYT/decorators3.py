"""
Using the same decorator for multiple functions
"""


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper function executed before {original_function.__name__}")

        return original_function(*args, **kwargs)

    return wrapper_function


# display = decorator_function(display) -> equivalent to what's below (17 - 18)
@decorator_function
def display():
    print('Display function ran')


@decorator_function
def display_info(name, age):
    print(f"display_info ran with arguments ({name},{age})")


display_info('Bishal', '21')

display()
