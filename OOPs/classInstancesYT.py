class Employee:
    raise_amount = 1.04 #this can be accessed from class as well as instances 
    def __init__(self,first,last,company, pay):
        self.first = first 
        self.last = last 
        self.email = f'{first}.{last}@{company}.com'
        self.pay = pay 
    
    def full_name(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) 
        

emp1 = Employee("Bishal","Chettri","WatchGuard",3400) 
emp2 = Employee("Snowden","Edward","NSA",2230)

print(emp1.email)
print(emp2.email)

print(emp1.pay) 
emp1.apply_raise() 
print(emp1.pay)

#these two are equivalent statements
print(Employee.full_name(emp1)) 
print(emp1.full_name())
