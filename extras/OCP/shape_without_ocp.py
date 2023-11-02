class Shape:
    def __init__(self, **kwargs):
        if kwargs['shape_type'] == 'circle':
            self.shape_type = 'circle'
            self.radius = kwargs['radius']
        elif kwargs['shape_type'] == 'rectangle':
            self.shape_type = 'rectangle'
            self.length = kwargs['length']
            self.breadth = kwargs['breadth']

    def area(self):
        if self.shape_type == 'circle':
            return 3.14 * (self.radius ** 2)
        elif self.shape_type == 'rectangle':
            return self.length * self.breadth


circle1 = Shape(shape_type='circle', radius=5)
rectangle1 = Shape(shape_type='rectangle', length=8, breadth=10)

print(circle1.area())
print(rectangle1.area())
