class Employee:
    num_of_emps = 0 
    raise_amount = 1.04  # this can be accessed from class as well as instances

    def __init__(self, first, last, company, pay):
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@{company}.com'
        self.pay = pay

        Employee.num_of_emps += 1 

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # self.pay = int(self.pay * self.raise_amount)


emp1 = Employee("Bishal", "Chettri", "WatchGuard", 3400)
emp2 = Employee("Snowden", "Edward", "NSA", 2230)


print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)


emp1.raise_amount = 1.05 #changes raise_amount only for that instance

print(emp1.__dict__)  # gives the attributes and values in dictionary format

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

'''
Say you want to create a class variable which is common for all instances 
like No of employees 
'''

print(Employee.num_of_emps)