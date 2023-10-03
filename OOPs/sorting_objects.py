'''
We are given a list of employee objects 
We need to sort it on the basis of their salary
'''


class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def __repr__(self):
        return f'<Employee ({self.name}, {self.salary})>'

    def __str__(self):
        return f'<Employee Object containing {self.name} {self.salary}>'


emp_list = [] #storing the Employee objects here

emp_list.append(Employee('Snowden',4000))
emp_list.append(Employee('Turing',1500))
emp_list.append(Employee('Oppenheimer',6000))
emp_list.append(Employee('Hawking',9000))
emp_list.append(Employee('Robin',1900))
emp_list.append(Employee('Beethoven',8000))


# sorting the list based on salary
emp_list = sorted(emp_list,key = lambda emp_obj: emp_obj.salary)

print("The salary from low to high with the employees are as: ")

for emp in emp_list:
    print(emp.name,emp.salary)


