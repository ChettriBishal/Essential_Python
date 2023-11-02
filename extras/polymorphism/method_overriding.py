"""
Method Overriding -> Runtime Polymorphism
"""


class Employee:
    def work(self):
        pass


class Developer(Employee):
    def work(self):
        print("Programming")


class Manager(Employee):
    def work(self):
        print("Managing Employees")


class TechSupport(Employee):
    def work(self):
        print("Managing devices and systems")


dev = Developer()
dev.work()

my_manager = Manager()
my_manager.work()
