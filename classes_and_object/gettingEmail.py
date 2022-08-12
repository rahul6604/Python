from unicodedata import name


class Student:
    fname = "name"
    lname = "last"
    year = 1971
    course = "xyz"
    def setData(self):
        self.fname = input("Enter your first name: ")
        self.lname = input("Enter your last name: ")
        self.year = int(input("Enter year of admission: "))
        self.course = input("Enter your subscribed course: ")
    @property
    def email(self):
        f = self.fname.lower()
        l = self.lname[0].lower()
        c = self.course.lower()
        return f"{f}{l}.{c}{self.year}@iujaipur.edu.in"
    @email.setter
    def email(self,val):
        name = val.split(".")[0]
        self.fname = name[0:len(name) -1].capitalize()
        self.lname = "None"
        self.course = val.split(".")[1][0:-4]
        self.year = val.split("@")[0][-4:]
    def getData(self):
       
        print("Name: ",self.fname,self.lname)
        print("Year: ",self.year)
        print("Course: ",self.course)

x =Student()
# x.email = "rahuls.btech2020@iujaipur.edu.in"
x.setData()
print(x.email)