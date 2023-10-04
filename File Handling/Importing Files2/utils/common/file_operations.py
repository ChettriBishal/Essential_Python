def save_to_file(content,filename):
    with open(filename,"w") as file:
        file.write(content)


def read_file(filename):
    with open(filename,"r") as file:
        for line in file.readlines():
            print(line) 

print(__name__)