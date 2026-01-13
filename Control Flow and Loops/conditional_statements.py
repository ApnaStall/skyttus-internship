# Check voting eligibility
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Grade calculator
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# Traffic light simulation
signal = input("Enter traffic light color (Red/Yellow/Green): ").lower()
if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("Go")
else:
    print("Invalid signal")

# ATM withdrawal check
balance = int(input("Enter account balance: "))
withdraw = int(input("Enter withdrawal amount: "))
if withdraw <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")

# Check if number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Check if number lies within a range
num = int(input("Enter number: "))
if 10 <= num <= 50:
    print("Number is within range")
else:
    print("Number is outside range")

# Username & password verification
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "123":
    print("Login successful")
else:
    print("Invalid credentials")

# Electricity bill calculator
units = int(input("Enter units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10
print("Electricity bill:", bill)

# Simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

# Check type of triangle
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
