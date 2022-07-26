class Number:
    def sum(self):
        return self.a + self.b

class ComplexNumber:
    def setData(self):
        self.real = int(input("Enter real part of complex number: "))
        self.img = int(input("Enter imaginary part of complex number: "))
    def showData(self):
        print(f"{self.real} + {self.img}i") #fstring
x= Number()
x.a =4;
x.b = 5;
print(x.sum())

p = ComplexNumber()
p.setData()
p.showData()
