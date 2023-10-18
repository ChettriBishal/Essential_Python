from collections import deque


def first_example():
    def greet():
        friend = yield  # suspend the function
        print(f'Hello {friend}')

    g = greet()
    g.send(None)  # priming the generator -> runs up to the section before the `yield`
    g.send('Snowden')


def second_example():
    friends = friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

    # these type of generators are known as co-routines
    # because they take in data and can be suspended
    def friend_upper():
        while friends:
            friend = friends.popleft().upper()
            greeting = yield  # suspend until we get some data
            print(f'{greeting} {friend}')

    def greet(g):
        g.send(None)  # priming the generator
        while True:
            greeting = yield
            g.send(greeting)

    """
    the greet() above can be replaced with
    def greet(g):
        yield from g 
    """

    greeter = greet(friend_upper())
    greeter.send(None)  # prime the greeter generator
    greeter.send('Hello')
    print('Multitasking')
    greeter.send('How are you?')


second_example()
