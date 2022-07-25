l1 = [1,2,3,4,5]
for item in l1:
    if (item%2==0):
        print(item)
    
n =int(input("Enter a number: "))

for i in range(1,11): # including,excluding
    print(n ,"X",i,"=",n*i)

# while loop
i = 1
n = int(input("Enter a number: "))
print("The square of numbers till:", n, "is")
while (i!=n):
    print(i*i)
    i=i+1


# for loop with else
for i in range(1,10):
    if(i == 7):
        break
    else:
        print(i)
    
else:
    print("Done")  #It will only be executed if the loop is not breaked