# from ..find import NotFoundError
# if we give the statement above it will result in circular import
def save_to_file(content, filename):
    with open(filename,"w") as file:
        file.write(content) 


def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read() 
        return contents 

print(__name__)