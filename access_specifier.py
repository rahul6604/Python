class Employee:
    company="Mircrosoft"
    _experience = 5 #protected variable
    __salary= 50000 #private variable
rahul = Employee()
print(rahul.company)
print(rahul._experience)
print(rahul._Employee__salary) #Accessing private variable