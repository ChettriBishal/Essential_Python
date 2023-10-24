from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    def walk(self):
        print("Walking...")

    @abstractmethod
    def num_legs(self): # the base classes must have this method defined else we can't construct those classes
        return 4


class Dog(Animal):
    def num_legs(self):
        return 4


class Monkey(Animal):
    def __init__(self,name):
        self.name = name

    def num_legs(self):
        return 2


# a = Animal()
noida = Monkey('maestro')
print(noida.num_legs())
