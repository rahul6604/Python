class Employee:
    sal = 5000
    bonus = 500
    @property #getter
    def total(self):
        return self.sal + self.bonus
    def showData(self):
        print("Salary: ",self.sal)
        print("Bonus: ",self.bonus)
        print("Total Salary: ",self.total)
    @total.setter
    def total(self,val):
        self.bonus = val - self.sal

e = Employee()
e.total = 4000
e.showData()