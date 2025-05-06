class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating multiple objects
person1 = Person("Aliya", 33)
person2 = Person("Babar", 20)

# Accessing attributes
print(person1.name, person1.age)  
print(person2.name, person2.age)  
person1.age = 31
print(person1.age)  
