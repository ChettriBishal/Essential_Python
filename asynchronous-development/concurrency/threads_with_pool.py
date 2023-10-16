import time
from concurrent.futures import ThreadPoolExecutor


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

start = time.time()

# create two threads in these pool of threads
# with this context manager we don't have to wait for pool.shutdown()
with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(ask_user)
    pool.submit(complex_calculation)

print(f'Two threads total time: {time.time() - start}')
