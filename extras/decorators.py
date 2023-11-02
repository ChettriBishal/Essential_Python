from functools import wraps
import time


def timer_decorator(func):
    wraps(func)

    def wrapper(*args, **kwargs):
        start = time.time()
        val = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start} s")
        return val

    return wrapper


@timer_decorator
def find_sum(arr):
    res = 0
    for x in arr:
        res += x
    return res


my_arr = [x ** 2 for x in range(2000000)]

print(find_sum(my_arr))
