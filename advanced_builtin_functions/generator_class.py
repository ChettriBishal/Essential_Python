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


l = FirstHundredGenerator()
print(next(l))
'''
for i in FirstHundredGenerator():
    print(i) 
this gives you an error too

'''

# this is not a generator though it's an iterator
class FirstFiveIterator:
    def __init__(self):
        self.numbers = [1, 2, 3, 4, 5]
        self.i = 0

    def __next__(self):
        if self.i < 5:
            curr = self.numbers[self.i]
            self.i += 1
            return curr
        else:
            raise StopIteration()


first_five = FirstFiveIterator()
print(first_five)
print(next(first_five))
print(next(first_five))

'''
but we can't do this

for val in first_five:
    print(val) 
    
because it's not a generator. 

Object is not iterable

Iterator and Iterable are different things. 
'''
