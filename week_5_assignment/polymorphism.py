#!/usr/bin/env python3
"""
A class to demonstrate polymorphism in Python.
This class includes two base classes: Animal and Vehicle,
and two derived classes for each base class: Dog and Bird for Animal,
and Car and Plane for Vehicle.
"""

class Animal:
    """
    Base class for animals, defining the move method.
    """
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Dog(Animal):
    """
    A class to represent a dog. Inherits from Animal.
    """
    def move(self):
        print("Running")


class Bird(Animal):
    """
    A class to represent a bird. Inherits from Animal.
    """
    def move(self):
        print("Flying")


class Vehicle:
    """
    Base class for vehicles, defining the move method.
    """
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")


class Car(Vehicle):
    """
    A class to represent a car. Inherits from Vehicle.
    """
    def move(self):
        print("Driving")


class Plane(Vehicle):
    """
    A class to represent a plane. Inherits from Vehicle.
    """
    def move(self):
        print("Flying")



if __name__ == "__main__":
    dog = Dog()
    bird = Bird()
    car = Car()
    plane = Plane()
    
    dog.move()
    bird.move()
    car.move()
    plane.move()
