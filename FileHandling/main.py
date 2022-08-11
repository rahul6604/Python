# Types of File:-
# 1. Binary File
# 2. Text File

# Open, reading, printing and closing a file
f = open("note.txt","r")
text = f.read()
print(text)
f.close()

# Note:-
# read = read full file
# readline = read first line
# readlines = read all lines


# To read line wise
f2 = open("note.txt")
text = f2.readline()
print(text)
f.close()

# To read first n character
f3 = open("note.txt","r")
text = f3.read(4)
print(text)
f3.close()

# Modes of Opening File
# r = open for reading
# w = open for writing
# a = open for appending
# rb = open for reading in binary file

f4 = open("note2.txt","a")
f4.write(input("Enter Data Here: "))
f4.close()

# with statement
# No need to close the file 

with open("name","w") as f:
    f.write("Rahul")
    
# tell() = returns the current pointing character of the file
# seek() = changing the pointing character in the file

with open("text.txt","r") as f:
    print(f.tell())
    data = f.readline()
    print(data)
    f.seek(0)
    data = f.readline()
    print(data)

    
