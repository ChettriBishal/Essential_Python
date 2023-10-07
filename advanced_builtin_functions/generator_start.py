def ten_numbers():
    i = 0
    while i < 10:
        yield i
        i += 1

my_list = ten_numbers()
print(my_list)
print(next(my_list))
print(next(my_list))

range_obj = range(10)
print(next(range_obj))
