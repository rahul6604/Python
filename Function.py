# Factorial Function
def factorial(num):
    if(num==0):
        return 1
    else:
        return num * factorial(num-1)
# Addition Funtion
def sum(num):
    if (num == 0):
        return 0
    return num + sum(num - 1)

print(factorial(4))
print(sum(3))