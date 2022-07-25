# List in python
# List are mutable (changable)
from pyclbr import Function
from unittest import FunctionTestCase


Fruits = ["Apple","Orange","Mango"]
print(Fruits)
for item in Fruits:
    print(item)
Fruits[0] = "Graphs"
print(Fruits)
print(Fruits[::-1]) #Slicing

num = [1,5,3,8]
print(num)

# Sort Function
# Only applicable for number List
num.sort()
print(num)

#Reverse Function
num.reverse()
print(num)

# Append Function
num.append(99)
print(num)

#insert Function
num.insert(2,"Inserted")  #index,"value"
print(num)

# Pop Function
num.pop()
print(num)

#remove Function
num.remove("Inserted")
print(num)

# Extend Function
L1 = [1,2,3]
L2 = [4,5,6]
L4 = ["a","b","c"]
L3 = L1 + L2 +L4
print(L3)
L4.extend(L1)
print(L4)

# Index Function
print(L1)
print(L1.index(1))

# count function
List = [1,3,5,4,6,8,6,5,7,8,9,5]
print(List.count(5))

# clear Function
List.clear()
print(List)