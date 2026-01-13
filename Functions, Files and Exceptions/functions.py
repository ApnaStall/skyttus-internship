# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Function to reverse a string
def reverse_string(text):
    return text[::-1]

# Function to find factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Function to calculate simple interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

# Function to check palindrome
def is_palindrome(word):
    return word == word[::-1]

# Function to count vowels in a string
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

# Function to merge two lists
def merge_lists(list1, list2):
    return list1 + list2

# Function to find GCD of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find area of rectangle
def area_rectangle(length, width):
    return length * width

# Function to check Armstrong number
def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    total = 0

    for d in digits:
        total += int(d) ** power

    return total == num

# -----------------
# Function Testing
# -----------------

print("Prime check:", is_prime(7))
print("Reverse string:", reverse_string("Python"))
print("Factorial:", factorial(5))
print("Simple Interest:", simple_interest(1000, 5, 2))
print("Palindrome:", is_palindrome("madam"))
print("Vowel count:", count_vowels("Internship"))
print("Merged list:", merge_lists([1, 2], [3, 4]))
print("GCD:", gcd(48, 18))
print("Area of rectangle:", area_rectangle(5, 4))
print("Armstrong check:", is_armstrong(153))
