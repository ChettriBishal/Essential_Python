def prime_generator(bound):
    # your code starts here (delete the pass):
    for n in range(2,bound):
        for x in range(2,n):
            if n % x == 0:
                break
        else:
            yield n


primes = prime_generator(20)
for val in primes:
    print(val)