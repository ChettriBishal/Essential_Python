import time
from threading import Thread


####### SINGLE THREAD

def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')  # blocking operation (need to wait)
    greet = f'Hello, {user_input}'
    print(greet)
    print('ask_user: ', time.time() - start)


def complex_calculation():
    print('Started calculating...')
    start = time.time()
    k = [x ** 2 for x in range(20000000)]
    print('complex_calculation: ', time.time() - start)


# With a single thread, we can do one at a time—e.g.
start = time.time()
ask_user()
complex_calculation()
print('Single thread total time: ', time.time() - start, '\n\n')

thread1 = Thread(target=complex_calculation)
thread2 = Thread(target=ask_user)

start = time.time()
thread1.start()
thread2.start()

# asking our main thread to wait for these threads to complete
# blocking operations
thread1.join()
thread2.join()

print(f'Two threads total time: {time.time() - start}')
