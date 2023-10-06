class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    
    @property
    def average(self):
        return sum(self.marks) / len(self.marks)
    
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary
    
    
rolf = WorkingStudent("Rolf", "MIT", 15.50)
rolf.marks.append(57)
    
print(rolf.average)