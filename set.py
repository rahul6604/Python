# unordered
# immutable
# unindexed
# can't contain duplicates
s = {1,2,3}
print(type(s))
for i in s:
    print(i)
print(s)

# Methods

# len
print(len(s))

# add
s.add(0)
s.add(-5)
print(s)

# remove
s.remove(1)
print(s)

#pop
s.pop()
s.pop()
print(s)

# union 
s = s.union({4,8,7,'a'})
print(s)

# intersection
s = s.intersection({1,2,"a"})
print(s)

# clear
s.clear()
print(s)