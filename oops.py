from abc import ABC, abstractmethod

class Animal(ABC):                    #Abstactions
    def __init__(self, name):
        self.__name = name            #Encapsulation


    def get_name(self):
        return self.__name


    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):                      #Inheritance
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

#Polymorphism
for animal in[Dog("Tommy"), Cat("Mini")]:
    print(animal.get_name(), animal.sound())