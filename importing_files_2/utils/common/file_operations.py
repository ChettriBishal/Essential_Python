# this can be used when this file is only run as a module and not as a script
from ..find import NotFoundError  # Going to the parent


# from ...utils.find import NotFoundError
# from importing_files.utils.find import NotFoundError

def save_to_file(content, filename):
    with open(filename, "w") as file:
        file.write(content)


def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        return contents


print(__name__)
