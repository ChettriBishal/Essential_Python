friends = ['Snowden', 'Oppenheimer', 'Zuckerberg', 'Jobs', 'Seneca']

start_with_s = filter(lambda x: x[0] == 'S', friends)

start_with_s_2 = (x for x in friends if x.startswith('S'))

print(next(start_with_s))
print(next(start_with_s))

print(list(start_with_s_2))


def custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


start_with_s_3 = custom_filter(lambda x: x.startswith('S'), friends)
print(start_with_s_3)
print(list(start_with_s_3))
