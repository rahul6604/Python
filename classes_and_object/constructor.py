class Employee:
    company = "Google"
    def __init__(self):
        self.name = input("Enter employee name: ")
        self.age = int(input("Enter employee age: "))
    def showData(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Age: {self.age}")
        print(f"Employee company: {self.company}")
Rahul = Employee()
Rahul.showData()