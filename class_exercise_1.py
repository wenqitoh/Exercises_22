class Dog:
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour = colour

    def print_details(self):
        return f"{self.name} is a {self.colour} dog aged {self.age}"

    def change_age(self, age):
        self.age = age


# main routine
dog1 = Dog("Spot", 12, "pink")
dog2 = Dog("Jazz", 7, "orange splotches")

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))

dog1.change_age(13)
dog2.change_age(81)

print(Dog.print_details(dog1))
print(Dog.print_details(dog2))

