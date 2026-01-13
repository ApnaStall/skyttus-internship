# Print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# Multiplication table for a given number
num = int(input("Enter a number for multiplication table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# Factorial of a number
n = int(input("Enter a number to find factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial:", factorial)

# Generate first N Fibonacci numbers
N = int(input("Enter number of Fibonacci terms: "))
a, b = 0, 1
for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b
print()

# Check if a number is prime
num = int(input("Enter a number to check prime: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

print("Prime" if is_prime else "Not Prime")

# Reverse a number
num = int(input("Enter a number to reverse: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number:", reverse)

# Count digits in a number
num = int(input("Enter a number to count digits: "))
count = 0
while num > 0:
    count += 1
    num //= 10
print("Number of digits:", count)

# Sum of even numbers between 1 and 100
total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i
print("Sum of even numbers (1-100):", total)

# Print a pyramid pattern
rows = int(input("Enter number of rows for pyramid: "))
for i in range(1, rows + 1):
    print("*" * i)

# Find all divisors of a number
num = int(input("Enter a number to find divisors: "))
print("Divisors:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i)
