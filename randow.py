import random

from scipy import rand
random_number= random.randint(0,4) # print random number between 0 and 4 (including 0 and 4)
print(random_number)

ran =random.random() #print number between 0 and 1
print(ran)

lst = ['python', 'c', 'c++', 'ruby', 'java' ]
print(random.choice(lst))