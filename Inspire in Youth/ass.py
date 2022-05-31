class Person:
    def __init__(self,name,dob,height,weight):
        self.name= name
        self.dob=dob
        self.height=height
        self.weight=weight
    def print_age(self):
        self.age=2022-self.dob
        print(f"You are {self.age}years old.")

    def print_Bmi(self):
        self.Bmi=self.height/pow(self.weight,2)
        print(f"Your Bmi is{self.Bmi}")
