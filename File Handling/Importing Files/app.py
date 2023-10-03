# whatever we import is known as a module

# import file_operations
# file_operations.save_to_file("Bishal", "data.txt")

# from file_operations import save_to_file
# save_to_file("Snowden","data.txt")

from utils.file_operations import save_to_file, read_file

save_to_file("Snowden","data.txt")
read_file("data.txt")

