def collatz(n):
    while True:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n
        if n == 1:
            break


for i in collatz(300):
    print(i, end=' ')
