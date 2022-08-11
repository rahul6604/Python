def name(normal, *args):
    print(f"Author: {normal}")
    for item in args:
        print(item)
me = "Rahul"
name(me,"Vijay","Anirudh","Nitish")

# If you want to give normal variable as an arugument, then it must be the first one

def lang(default, **kwargs):
    print(f"Author : {default}")
    for key,value in kwargs.items():
        print(f"{key} = {value}")

my_lang = "C++"
languages = {"Vijay":"Python", "Anirudh":"c", "Nitish": "Stock Market"}
lang(my_lang,**languages)

# args for tuple and list
# kwargs for dictionary