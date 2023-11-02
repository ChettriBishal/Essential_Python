class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Initialised the Person instance")

    def __str__(self):
        return f'<{self.name}, {self.age}>'


person1 = Person("Edward Snowden", 42)
print(person1)
print("--------------------------------")


class Employee:
    def __new__(cls, *args, **kwargs):
        instance = super(Employee, cls).__new__(cls)
        print("Creates a new Employee instance")
        return instance

    def __init__(self, name, domain):
        self.name = name
        self.domain = domain
        print("Initialized the Employee instance")

    def __str__(self):
        return f"<{self.name},{self.domain}>"


employee1 = Employee("Edward Snowden", "Cybersecurity")
print(employee1)
