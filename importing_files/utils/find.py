from .common.file_operations import save_to_file #gives error if we singly run this as main

'''
To only run this file separately 
from common.file_operations import save_to_file

but when we invoke it via another module 
"." tells that the file is inside the current working directory

'''

def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:   
            return i 
    raise NotFoundError(f"{expected} is not present in the iterable")


class NotFoundError(Exception):
    pass 

print(__name__)