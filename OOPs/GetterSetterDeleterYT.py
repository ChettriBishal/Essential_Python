class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @full_name.deleter
    def full_name(self):
        print('Name deleted!')
        self.first = None
        self.last = None

    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'


emp_1 = Employee("John", "Doe")
emp_1.first = 'Jim'
print(emp_1.email)  # we can access email like an attribute -> getter

emp_1.full_name = 'Bishal Chettri'  # possible because of setter
print(emp_1.full_name)
print(emp_1.email)

del emp_1.full_name  # deleter in play
print(emp_1.full_name)
