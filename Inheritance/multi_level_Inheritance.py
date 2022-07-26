class manager:
    # @staticmethod
    def call(self):
        print("I am a Manager")
class Employee(manager):
    # @staticmethod
    def call(self):
        super().call()
        print("I am an Employee")
class Programmer(Employee):
    # @staticmethod
    def call(self):
        super().call()
        print("I am an Employee")
m = manager()
e = Employee()
p = Programmer()
print("Calling manager...")
m.call()
print("\n")
print("Calling employee...")
e.call()
print("\n")
print("Calling programmer...")
p.call()