fruits = {"oranges", "mangoes", "apples"}
print(fruits)
print(fruits)
print(fruits)
print(pow(2 ,3))

#function to replace character in a string.
def replace_in(phrase):
    word = ""
    for letter in phrase: 
        if letter.lower() in "aeiou":
            word = word + "g"
        else:
            word = word + letter
    return word
print(replace_in(input("enter phrase:")))
