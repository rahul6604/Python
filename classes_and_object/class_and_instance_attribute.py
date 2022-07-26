class Employee:
    Company = "Google" #class Attribut
    def showData(self):
        print(f"Company: {self.Company}")
        print(f"Age: {self.age}") #instance attribute
        print(f"Salary: {self.salary}")
        
ram = Employee()
ram.age = 45
ram.salary = 45000
ram.showData() #Employee.showData(ram)
