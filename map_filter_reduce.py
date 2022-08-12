'''''''''''''''''''''''''''Map'''''''''''''''''''''''
lst = ["44","23","56"]

# for i in range(len(lst)):
#     lst[i] = int(lst[i])

lst =list(map(int,lst))

lst[2] = lst[2]+4
print(type(lst))
print(lst)

num = [2,4,6,8]
squar_list = list(map(lambda x:x*x, num))
print(squar_list)

def square(x):
    return x*x
def cube(x):
    return x*x*x

func = [square, cube]
def get(x):
    return x(i)
for i in range(4):
    # l = list(map(get,func))
    l = list(map(lambda x:x(i),func))
    print(l)

# filter() method: This method returns a new array containing the elements that passes a certain test performed. on an original array. ...
# map() method: This method is used to apply a function on every element in an array and returns a new array of.
# Reduce: can be used to return almost anything. It is often used to return a single number, like an sum, but it can also be used to combine the logic of Map and Filter to return an array of values matching certain criteria. 

'''''''''''''''''''''''''''Filter'''''''''''''''''''''''
def greater(x):
    return x>5
num = list(filter(greater,num))
print(num)


'''''''''''''''''''''''''''Reduce'''''''''''''''''''''''
from functools import reduce
n = [1,2,3,4]
sum = reduce(lambda x,y:x+y,n)
print(sum)


