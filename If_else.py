n = int(input("Enter a number: "))
if (n%2==0):
    print(n, "is a even number")
else:
    print(n, "is a odd number")

c = input("Enter a character; ")
if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
    print(c, "is a vowel")
elif(c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'):
    print(c, "is a vowel")
else:
    print(c,"is not a vowel")
