def greet():
    print('Hello')


# function which accepts another function as an argument
k = greet
k()


def before_and_after(func):
    print('Before')
    func()
    print('After')


before_and_after(lambda: 'Hello')
