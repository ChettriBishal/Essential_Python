class Employee:
    def work(self):
        pass


class Developer(Employee):
    def work(self):
        print("Programming")


class Manager(Employee):
    def work(self):
        print("Management")


class TechSupport(Employee):
    def work(self):
        print("Managing devices and systems")


def perform_work(employee):
    employee.work()


# more focused on the function than the object

dev = Developer()
perform_work(dev)

manager = Manager()
perform_work(manager)
