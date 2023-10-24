class Animal:
    def hungry(self):
        print('I want to eat {}!'.format(self.get_favourite_food()))


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def get_favourite_food(self):
        return 'ribs'


d1 = Dog('ronny')
print(d1.get_favourite_food())