
# import math
from math import sqrt
class Calculator:
    @staticmethod
    def square(num):
        return num*num
    @staticmethod
    def sq_root(num):
        return sqrt(num)
n = Calculator()
print(n.square(4))
print(n.sq_root(4))
print(sqrt(4))