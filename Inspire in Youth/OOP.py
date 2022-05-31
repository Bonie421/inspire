#OOP
#Defining a class and its attributes.
#Creating instances (objects)of a class
#Class methods (functions belonging to a class)
#Inheritance & polymorphism.
#Method overriding.
class Dog:
    def __init__(self, no_of_eyes, color, no_of_legs, fur ):
        self.no_of_eyes = no_of_eyes
        self.color = color
        self.no_of_legs = no_of_legs
        self.fur = fur

    def bark(self):
        print("Woof! Woof!")
    def fart(self):
        print("frrrrtttzzz!!!")

german_shephard = Dog(no_of_eyes=2, color='Grey', no_of_legs=5, fur='alot')
dodger = Dog(no_of_eyes=1, color='white', no_of_legs=4,fur='thick')
dobberman = Dog(2, 'Brown', no_of_legs=4, fur='less')
chiwawa = Dog(4, "Blue", no_of_legs=8, fur='much fur')

print(german_shephard.color, german_shephard.no_of_eyes, german_shephard.fur, german_shephard.no_of_legs)
print(dodger.color, dodger.no_of_eyes, dodger.no_of_legs, dodger.fur) 
print(dobberman.color, dobberman.no_of_eyes, dobberman.fur, dobberman.no_of_legs)
print(chiwawa.color, chiwawa.no_of_eyes, chiwawa.fur, chiwawa.no_of_legs)

dodger.color = "yellow"
print(dodger.color)
dodger.bark()
dobberman.fart()