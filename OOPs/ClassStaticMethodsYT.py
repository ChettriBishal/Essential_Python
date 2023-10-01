import datetime

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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # creating an alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # invoking the constructor of the class passed
        return cls(first, last, "company", pay)
        # equivalent to this
        # return Employee(first,last,"company",pay)
    
    @staticmethod
    def is_workday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False 
        return True 


emp1 = Employee("Bishal", "Chettri", "WatchGuard", 3400)
emp2 = Employee("Snowden", "Edward", "NSA", 2230)

Employee.set_raise_amt(1.05)
# Employee.raise_amount = 1.05

# we can even run that class method from an instance

# emp1.set_raise_amt(1.06)
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, "company", 70000)

new_emp_1 = Employee.from_string(emp_str_1) 

print(new_emp_1.email)
print(new_emp_1.pay)


#Checking static method

my_date = datetime.date(2023,6,10)
print(Employee.is_workday(my_date))