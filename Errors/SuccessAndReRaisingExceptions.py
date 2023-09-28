"""
It can sometimes be handy to do something with an exception (handle it), but then not silence it.

For example, if an exception is raised in a function and you catch it:
"""


def get_value(my_dict, key):
    try:
        k = my_dict[key]
        return k
    except KeyError:
        print('Incorrect values provided')
        raise  # Makes the tracebrack visible
    finally:
        print("Coming out of the function")


"""
The `raise` keyword here, used without an error class after it, just re-raises the exception that was caught in the current `except` block.
"""

bis_dict = {'Name': 'Bishal', 'Age': 21}

# print(get_value(bis_dict,'Year'))

'''
Using else block instead of finally
It will come to this block if it doesn't catch any exception and provided there's no return value in try block
'''


def get_value2(my_dict, key):
    try:
        val = my_dict[key]
        # return k
    except KeyError:
        print('Incorrect values provided')
    else:
        print("Inside the else block")
        return val  # now returning the value of


print(get_value2(bis_dict, 'Name'))
