"""
yield -> not just a statement, it's also an expression that returns a value back to you

Generators are not just plausible functions, they are bidirectional pipelines

Just like generators can yield a value up to its caller, the caller can send value back down to a generator.

Asyncio co-routines under the hood is designed using generators
"""

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


def example_worker():
    w = worker(str)  # generator object
    w.send(None)  # generator priming
    w.send([(1,), (2,), (3,)])
    print(next(w))
    print(next(w))
    print(next(w))
    w.send([(4,), (5,)])
    print(next(w))
    print(next(w))
    # w.throw(ValueError)


example_worker()
