class Worker:
    def work(self):
        pass

    def eat(self):
        pass

'''
Now, you have two types of workers: Manager and Programmer. 
According to the Interface Segregation Principle, 
you should avoid forcing both types of workers to implement methods they don't need.
Instead, create specific interfaces for each type:
'''

class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Manager(Workable, Eatable):
    def work(self):
        return "Manager is working"

    def eat(self):
        return "Manager is eating"

class Programmer(Workable):
    def work(self):
        return "Programmer is working"
