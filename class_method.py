class Employee:
    Total_Salary = 4000
    bonus = 400
    def showData(self):
        print(self.Total_Salary)
        print(self.bonus)

    def changeSal(self,sal): #instance member
        self.Total_Salary = sal

    def changeBonus(self,bon): #instance member
        self.bonus = bon

    def change_class_sal(self,sal): #class member
        self.__class__.Total_Salary = sal

    @classmethod 
    def change_class_bonus(cls,bon): #class member
        cls.bonus = bon
# -----Driver Program-----
e = Employee()
# e.showData()
# print(Employee.bonus)
# e.change_class_bonus(10)
# print(Employee.bonus)
# e.showData()
# e.change_class_sal(4)
# e.showData()
# print(Employee.Total_Salary)

