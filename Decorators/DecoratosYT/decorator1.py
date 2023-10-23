"""
Decorators are a way to dynamically alter the functionality of your functions.
So for example, if you wanted to log information when a function is run, you could use a decorator to add this
functionality without modifying the source code of your original function.
"""


def decorator_function(original_function):
    def wrapper_function():
        return original_function()

    return wrapper_function


def display():
    print('Display function ran')


decorated_display = decorator_function(display)
decorated_display()  
