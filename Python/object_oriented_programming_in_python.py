# %%
# Object Oriented Programming (OOP) in Python

from typing import Any


class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    def sound(self):
        return "Bark!"

    def sit(self):
        return f"{self.name} is now sitting."

my_dog = Dog("Rex", 3)
another_dog = Dog("Ziggy", 5)
print("Object address: ", my_dog)
print("Object address: ", another_dog)
# %%
print(my_dog.name, my_dog.age)
print(my_dog.sound())

print(another_dog.name, another_dog.age)
print(another_dog.sound())

print(my_dog.species)
print(another_dog.species)

# %%
my_dog.name = "Azorel"
my_dog.age = 4
print(my_dog.name, my_dog.age)
# %%
# Inheritance
class Terrier(Dog):
    pass

my_terrier = Terrier("Max", 1)
print(my_terrier.name, my_terrier.age)
print(my_terrier.sound())
print(my_terrier.sit())
# %%
# Overriding methods
class GoldenRetriever(Dog):
    def sound(self):
        return "Woof!"

my_golden = GoldenRetriever("Buddy", 2)
print(my_golden.name, my_golden.age)
print(my_golden.sound())

my_dog2 = Dog("Rex", 3)
print(my_dog2.sound())
# %%
class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__("Canis familiaris")
        # FYI: super("Animal", self).__init__("Canis familiaris")
        self.name = name
        self.age = age

    def sound(self):
        return "Bark!"
    
    def sit(self):
        return f"{self.name} is now sitting."

# GoldenRetriever -> Dog -> Animal
class GoldenRetriever(Dog):
    def sound(self):
        return "Woof!"

# Animal -> Cat
class Cat(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__("Felis catus")
        self.name = name
        self.age = age
        self.fur_color = fur_color

    def sound(self):
        return "Meow!"
    
    def get_fur_color(self):
        return self.fur_color

# %%
my_dog = Dog("Rex", 3)
my_terrier = Terrier("Max", 1)
my_golden = GoldenRetriever("Buddy", 2)
my_cat = Cat("Kitty", 4, "white")
# %%
def play_sound(animal):
    print(animal.sound())

play_sound(my_dog)
play_sound(my_terrier)
play_sound(my_golden)
play_sound(my_cat)
# %%
# Method resolution order (MRO)
print(Dog.__mro__)
print(GoldenRetriever.mro())

print(int.__mro__)
# %%
# isinstance() vs type()
print(type(my_dog))
print(type(my_terrier))
print(type(my_golden))
print(type(my_cat))
# %%
print(Dog.__mro__)
animal = Animal("Canis familiaris")
print(isinstance(animal, Dog))
print(isinstance(my_dog, Dog))
print(isinstance(my_dog, Animal))
print(isinstance(my_dog, GoldenRetriever))
print(isinstance(my_golden, GoldenRetriever))
print(isinstance(my_golden, Dog))
print(isinstance(my_golden, Animal))
# %%
class Engine:
    def start(self):
        return "Engine is starting."

class Electric:
    def charge(self):
        return "Battery is charging."

class HybridCar(Electric, Engine):
    pass

print(HybridCar.__mro__)
# %%
class Vehicle:
    def __init__(self, model):
        self.model = model
        self.__id = 123 # private attribute
        self._speed = 0 # "protected" attribute
    
    # private method
    def __check_internal_components(self):
        return "Internal check passed."

    # protected method
    def _show_speed(self):
        return f"Current speed is {self._speed} km/h."
    
    # getter and setter for private attribute
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id

my_vehicle = Vehicle("Tesla")
print(my_vehicle.model)
print(my_vehicle._speed)
#print(my_vehicle.__id)
# %%
class Car(Vehicle):
    def __init__(self, model):
        super().__init__(model)
        print(self.model)
        print(self._speed)
        self.id = "akfg"

my_car = Car("Dacia")
my_car._show_speed()
#my_car.__check_internal_components()
# %%
# Name mangling = how Python handles private attributes and methods
# _ClassName__attribute_name
# _ClassName__method_name
# NOTE: It's not a security feature, it's just a way to avoid name clashes
print(my_vehicle._Vehicle__id)
print(my_vehicle._Vehicle__check_internal_components())
# %%
# Summary
# - OOP in Python
# - Encapsulation
# - Private and protected attributes and methods
# - Name mangling
# - Inheritance
# - Polymorphism
# - Overriding methods
# - Method resolution order (MRO)
# - isinstance() vs type()
# %%
# Type hinting
def compute_sum_int(a: int, b: int) -> int:
    return a + b

c = compute_sum_int(3, 4)
print(c)

d = compute_sum_int(3.5, 4.5)
print(d)
# %%
