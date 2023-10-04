from .common.file_operations import save_to_file #relative path
'''
If I run this script singularly then 

from common.file_operations import save_to_file #relative path

cause common becomes the root directory

'''

# print(__name__)
class NotFoundError(Exception):
    def __init__(self, message):
        super().__init__(message) 


def find_in(iterable, key):
    for item in iterable:
        if item == key:
            return f'{item} found!' 
    return NotFoundError(f'{key} not found')

print(__name__)