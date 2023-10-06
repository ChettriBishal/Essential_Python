'''
You can pass first class functions as arguments to another function. All function in python are first class.
'''
def greet():
    print("Hello")

#assign function to a variable
#greet -> doesn't do anything

hello = greet
hello() #invokes the function

def average(arr):
    return sum(arr)/ len(arr)

avg = lambda arr: sum(arr)/ len(arr)
tot = lambda arr: sum(arr)
top = lambda arr: max(arr)

operations = {
    "average": avg,
    "total": tot,
    "top": top
}

students = [
    {"name": "Rolf", "grades": (67,98,95, 100)},
    {"name": "Bob", "grades": (56,78,80,90)},
    {"name": "Snowden", "grades": (88, 89,96,99)}
]

#print the average total and top morks for every student
for student in students:
    name = student['name']
    grades = student['grades']
    print(name, avg(grades), tot(grades), top(grades))

    '''
    considering the following scenario
    operation = input("Enter 'average','total' or 'top': ")
    operation_function = operations[operation]

    print(operation_function(grades))
    '''