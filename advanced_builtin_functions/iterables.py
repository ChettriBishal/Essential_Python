class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        while self.number < 100:
            curr = self.number
            self.number += 1
            return curr
        else:
            raise StopIteration()

    # in this case generator is both an iterator and an iterable
    def __iter__(self):
        return self


print(sum(FirstHundredGenerator()))  # prints 4950

# for i in FirstHundredGenerator():
#     print(i)


class AnotherIterable:
    def __init__(self):
        self.cars = ['BMW', 'Range Rover']

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]


for car in AnotherIterable():
    print(car)

'''

class FirstHundredIterable:
    def __iter__(self):
        return FirstHundredGenerator()
    # placing it inside FirstHundredGenerator we just need to return self clearly


print(sum(FirstHundredIterable())) #prints 4950

for i in FirstHundredIterable():
    print(i)

'''
