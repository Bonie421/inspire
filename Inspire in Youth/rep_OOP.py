from inspect import *
from os import name
from xml.dom.xmlbuilder import DOMBuilder


class person:
    def __init__ (self, name, age):
        self.name=name
        self.age=age
    pass
    def details(self):
        print(f"My name is {self.name} and my age is {self.age}")
p1 = person("Bonnie",19)
p1.details()

    def birthday(self):
        self.age = self.

class Employee(person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        def details(self):
            print(f"My name is {self.name} , my age is {self.age} and my salary is {self.salary}")
p2 = Employee("Bonnie", 19, 500)
p2.details()

classes - name                 output name
         -DOB                  output age(calc DOB)
         -Height               output BMI(Calc from height and weight)
         -weight

student -class                  output class
        -fav subj               output name 
                                output _Subj 

teacher-subj                    output name 
       -salary                  output subj
                                output salary