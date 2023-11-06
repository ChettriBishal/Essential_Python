from abc import ABC, abstractmethod

from math import pi


class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type = shape_type

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, height, breadth):
        super().__init__("rectangle")
        self.height = height
        self.breadth = breadth

    def area(self):
        return self.height * self.breadth


circle1 = Circle(4)
print(circle1.area())

rectangle1 = Rectangle(45, 33)
print(rectangle1.area())

print(id(circle1.area))
print(id(rectangle1.area))
