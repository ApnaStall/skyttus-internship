import math

# Car Class
class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, value):
        self.speed += value
        print("Car Speed after accelerating:", self.speed)

    def brake(self, value):
        self.speed = max(0, self.speed - value)
        print("Car Speed after braking:", self.speed)

# BankAccount Class
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Current Balance:", self.balance)

# Student Class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

# Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Employee Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

# Book Class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

# Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

# Laptop Class
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def apply_discount(self, percent):
        self.price -= self.price * (percent / 100)
        print("Laptop Price after discount:", self.price)

# Flight Class
class Flight:
    def __init__(self, flight_name, seats):
        self.flight_name = flight_name
        self.seats = seats

    def book_seat(self):
        if self.seats > 0:
            self.seats -= 1
            print("Seat booked. Remaining seats:", self.seats)
        else:
            print("No seats available")

# Shop Class
class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(product, "added to shop")

    def list_products(self):
        print("Products in shop:")
        for product in self.products:
            print("-", product)


# -------------------------
# Testing All Classes
# -------------------------
if __name__ == "__main__":

    car = Car("Toyota", "Innova")
    car.accelerate(30)
    car.brake(10)

    account = BankAccount(2000)
    account.deposit(500)
    account.withdraw(1000)
    account.show_balance()

    student = Student("Rahul", [80, 85, 90])
    print("Average Marks:", student.calculate_average())

    rect = Rectangle(10, 5)
    print("Rectangle Area:", rect.area())
    print("Rectangle Perimeter:", rect.perimeter())

    emp = Employee("Amit", 50000)
    emp.display_salary()

    book = Book("Python Basics", "John Doe", 399)
    book.display_details()

    circle = Circle(7)
    print("Circle Area:", circle.area())
    print("Circle Circumference:", circle.circumference())

    laptop = Laptop("HP", 60000)
    laptop.apply_discount(10)

    flight = Flight("Indigo", 2)
    flight.book_seat()
    flight.book_seat()
    flight.book_seat()

    shop = Shop()
    shop.add_product("Laptop")
    shop.add_product("Mobile")
    shop.list_products()
