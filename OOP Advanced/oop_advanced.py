# Base class Animal and subclasses Dog and Cat
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Vehicle → Car → ElectricCar hierarchy
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def fuel(self):
        print("Car uses fuel")

class ElectricCar(Car):
    def fuel(self):
        print("Electric car uses electricity")

# Method Overriding (base & derived)
class Shape:
    def area(self):
        print("Area not defined")

class Square(Shape):
    def area(self):
        print("Area of square = side * side")

# Multiple Inheritance
class Camera:
    def feature(self):
        print("Camera feature")

class GPS:
    def feature(self):
        print("GPS feature")

class Smartphone(Camera, GPS):
    pass

# Polymorphism with Shapes
class Circle:
    def draw(self):
        print("Drawing Circle")

class Rectangle:
    def draw(self):
        print("Drawing Rectangle")

def draw_shape(shape):
    shape.draw()

# Bank System (Savings & Current Account)
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def display_balance(self):
        print("Balance:", self.balance)

class SavingsAccount(BankAccount):
    def interest(self):
        print("Savings account interest applied")

class CurrentAccount(BankAccount):
    def overdraft(self):
        print("Current account overdraft facility")

# Private Attributes with Getter & Setter
class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


# Teacher and Student Inheritance
class Teacher:
    def teach(self):
        print("Teacher is teaching")

class StudentPerson(Teacher):
    def study(self):
        print("Student is studying")


# MusicPlayer and Spotify
class MusicPlayer:
    def play(self):
        print("Playing music")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify")


# Demonstrate super()
class Company:
    def __init__(self, name):
        self.name = name

class Employee(Company):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


# ---------------------
# Testing All Concepts
# ---------------------
if __name__ == "__main__":

    # Animal
    dog = Dog()
    cat = Cat()
    dog.speak()
    cat.speak()

    # Vehicle
    ecar = ElectricCar()
    ecar.move()
    ecar.fuel()

    # Method Overriding
    sq = Square()
    sq.area()

    # Multiple Inheritance
    phone = Smartphone()
    phone.feature()   # follows MRO

    # Polymorphism
    draw_shape(Circle())
    draw_shape(Rectangle())

    # Bank System
    savings = SavingsAccount(5000)
    current = CurrentAccount(3000)
    savings.display_balance()
    savings.interest()
    current.display_balance()
    current.overdraft()

    # Encapsulation
    person = Person()
    person.set_age(25)
    print("Age:", person.get_age())

    # Inheritance
    student = StudentPerson()
    student.teach()
    student.study()

    # Method Overriding
    player = Spotify()
    player.play()

    # super()
    emp = Employee("Amit", 60000)
    emp.display()
