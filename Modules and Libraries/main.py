import random
import datetime
import math
import os

from mymath import add, subtract
from string_ops import to_upper, reverse_string
from shapes.circle import area as circle_area
from shapes.rectangle import area as rectangle_area

# Import custom math module
print("Add:", add(10, 5))
print("Subtract:", subtract(10, 5))

# String operations
print("Uppercase:", to_upper("skyttus"))
print("Reverse:", reverse_string("python"))

# Random integers
print("Random Numbers:", random.sample(range(1, 100), 5))

# Current date and time
now = datetime.datetime.now()
print("Current Date & Time:", now)

# Factorial
print("Factorial of 5:", math.factorial(5))

# Shapes package
print("Circle Area:", circle_area(7))
print("Rectangle Area:", rectangle_area(10, 5))

# Multiple functions from one module
print(add(3, 2))
print(subtract(8, 4))

# Shuffle list
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print("Shuffled List:", items)

# Date difference
date1 = datetime.date(2024, 1, 1)
date2 = datetime.date(2024, 1, 15)
print("Date Difference:", (date2 - date1).days, "days")

# List files in directory
print("Files in current directory:")
print(os.listdir("."))
