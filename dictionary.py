# mutable
# key-value pair
# cannot contain duplicate Key
# indexed
dict1 = {"key":"value", "tuple":(1,2,4),"list":[4,5,6], "marks":100}
for item in dict1:
    print(item, type(item))

print(dict1['key'])
# Methods

# items (used to print key-value pair)
print(dict1.items())

# keys (used to print key)
print(dict1.keys())

# update (used to update key-value pair in the dictionary)
dict1.update({"name":"Rahul"})
print(dict1.items())

# get (to get value by key)
print(dict1.get("name"))
# if item is not present in the dictionary, it return None (it won't through an error) 