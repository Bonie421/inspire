#dictionaries in python.
mydict = {
"book" : "dynamics",
"publisher" : "longhorn",
"year" : 2001
}

#accessing item.
x = mydict["year"]
print(x)

#accessing  using get()
y = mydict["year"]
print(y)

#All keys
x = mydict.keys()
print(x)

#All values
x = mydict.values()
print(x)

#printing all items in a dictionary
x = mydict.items()
print(x)

#checking if key exists
if "publisher" in mydict:
    print("publisher is one of the keys")