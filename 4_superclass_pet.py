"""creating super/parent class
Wen-Qi Toh
23/2/22"""


# Creates a superclass - Pet, as a parent of Cat and Dog
class Pet:  # General Class
    # These are common attributes to any Pet
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # method to print pet details
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


# child classes are specific classes containing attributes unique to that class
class cat(Pet): # add brackets containing the parent class
