class Complex:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __add__(self, other):
        result = Complex(0, 0)
        result.real_part = self.real_part + other.real_part
        result.imaginary_part = self.imaginary_part + other.imaginary_part
        return result

    def __str__(self):
        return f'<{self.real_part} + {self.imaginary_part} i>'


comp1 = Complex(3, 8)
comp2 = Complex(9, 3)

print(comp1)
print(comp2)

comp3 = comp1 + comp2
print(comp3)

snowden = "Edward " + "Snowden"
result = 3 + 7

print(snowden)
print(result)

