class Employee:
    company = "Google"
    @staticmethod
    def showData():
        print("This is an employee")
    def __init__(self):
        print("Employee is created")
    
class Programmer(Employee):
    @staticmethod
    def showData():
        print("This is a programmer")
    def __init__(self):
        print("Programmer is created")

a = Employee()
b = Programmer()
a.showData()
b.showData()
print(f"a: {a.company} \nb: {b.company}")