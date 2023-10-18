from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


# these type of generators are known as co-routines
# because they take in data and can be suspended

@coroutine
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield  # suspend until we get some data
        print(f'{greeting} {friend}')


async def greet(g):
    print('Starting...')
    await g  # this won't finish until the coroutine has ended
    print('Ending...')  # this won't display as the queue is still not empty


"""
def greet(g):
    g.send(None)  # priming the generator
    while True:
        greeting = yield
        g.send(greeting)
"""

greeter = greet(friend_upper())
greeter.send(None)  # prime the greeter generator
greeter.send('Hello')

greeting = input('Enter a greeting: ')
greeter.send(greeting)

greeting = input('Enter a greeting: ')
greeter.send(greeting)
