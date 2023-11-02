class Circle(object):
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * (self.radius ** 2)


a = Circle(6)
b = Circle(7)

print(a)
print(b)

print("----------------")

print("a is b:", a is b)
print("a.PI is b.PI:", a.PI is b.PI)

print("a.PI ID: ", id(a.PI))
print("b.PI ID: ", id(b.PI))
print("----------------")

print("Changing b.PI")
b.PI = 3.141592653

print("Has the value of a.PI changed? ")
print(f"a.PI {a.PI}")
print(f"b.PI {b.PI}")

print("a.PI ID: ", id(a.PI))
print("b.PI ID: ", id(b.PI))
print("----------------")

b.PI = a.PI

print("a.PI ID: ", id(a.PI))
print("b.PI ID: ", id(b.PI))
