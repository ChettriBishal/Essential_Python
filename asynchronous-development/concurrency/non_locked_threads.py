import time
import random

from threading import Thread

# adding random time between codes is known as fuzzing
# without fuzzing the code would look normal

# Don't use threads if you want the operations to happen sequentially

counter = 0


def increment_counter():
    global counter
    time.sleep(random.randint(0, 2))
    counter += 1
    time.sleep(random.randint(0, 2))
    print(f'Updated counter value: {counter}')
    time.sleep(random.randint(0, 2))
    print('---------------')


for x in range(10):
    my_thread = Thread(target=increment_counter)
    time.sleep(random.randint(0, 2))
    my_thread.start()

"""
OUTPUT
Updated counter value: 2
---------------
Updated counter value: 3
Updated counter value: 4
---------------
Updated counter value: 5
---------------
Updated counter value: 5
---------------
---------------
Updated counter value: 8
---------------
Updated counter value: 8
---------------
Updated counter value: 8
---------------
Updated counter value: 10
---------------
Updated counter value: 10
---------------

Process finished with exit code 0

"""
