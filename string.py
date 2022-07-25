#String Functions
from pyclbr import Function
from re import S


a="Ram" #string
b="he is ram"
# len Function
print(len(a)) # print the lenght of string

# endswith Function
end = a.endswith("m")
print(a.endswith("d"))

#count Function
c = a.count("a")
print(c)

#capitalize Function
test1 = "abc"
t1 = test1.capitalize()
print(test1)
print(t1)

#upper
test2 = "rahul"
t2 = test2.upper()
print(test2)
print(t2)

#isupper
test3="Rahul"
t2 = test3.isupper()
print(t2)
print(test3.isupper())

# strip Function
# Used to remove unwanted space from the string
s = "   This is      Taj  Mahal    "
print(s)
s.strip()
print(s)
print(s.strip())

