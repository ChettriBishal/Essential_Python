import math

for i in range(2,100):
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            print(f"{i} equals {j} * {i//j}")
            break 
    else: #did not encounter break
        print(f"{i} is a prime number")