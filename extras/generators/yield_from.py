"""
yield from facilitates the bidirectional nature of generators
"""


def another_generator():
    # yield from (x*x from x in range(5))
    for sq in (x * x for x in range(5)):
        yield sq


for val in another_generator():
    print(val)

print("-------------------")

from collections import deque


def worker(f):
    tasks = deque()
    value = None

    while True:
        batch = yield value
        value = None
        if batch is not None:
            tasks.extend(batch)
        else:
            if tasks:
                args = tasks.popleft()
                value = f(*args)


def quiet_worker(f):
    while True:
        w = worker(f)
        try:
            yield from w
        except Exception as exc:
            print(f"ignoring {exc.__class__.__name__}")


# caller <---> quiet_worker <---> worker

def example():
    w = quiet_worker(str)
    w.send(None)
    w.send([(1,), (2,), (3,)])
    print(next(w))
    print(next(w))
    print(next(w))


example()
