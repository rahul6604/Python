# sort by alphabets
lst = ["banana", "Apple", "graphes", "Orange"]
# It sorts capital letter first and then small letters
print(lst)
lst.sort()
print(lst)

#To reverse sort
lst.sort(reverse=True)
print(lst)

# to sort by number
lst2 = [3,2,5,1]
print(lst2)
lst2.sort()
print(lst2)

# to sort using a custom parameter
myFun =  lambda e : e['year']

cars = [{'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}]
cars.sort(key=myFun)
print(cars)