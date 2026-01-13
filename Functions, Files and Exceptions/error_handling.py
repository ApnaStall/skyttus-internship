# Handle division by zero
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

# Handle invalid integer input
try:
    num = int(input("Enter an integer: "))
    print("You entered:", num)
except ValueError:
    print("Error: Invalid integer input")

# Handle file not found error
try:
    file = open("Data/sample.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found")

# Multiple exception blocks
try:
    x = int(input("Enter number: "))
    y = int(input("Enter another number: "))
    print(x / y)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
except Exception:
    print("Some other error occurred")

# Use finally for resource cleanup
try:
    file = open("Data/test.txt", "w")
    file.write("Hello Python")
except Exception:
    print("Error occurred while writing file")
finally:
    file.close()
    print("File closed")

# Custom exception for invalid age
class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")
    print("Age is valid")
except InvalidAgeError as e:
    print(e)

# Handle IndexError
my_list = [10, 20, 30]
try:
    index = int(input("Enter index: "))
    print(my_list[index])
except IndexError:
    print("Error: Index out of range")

# Handle all possible errors with two numbers
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid number input")
except Exception:
    print("Unexpected error")

# Log errors to a file
try:
    x = int(input("Enter number: "))
    y = int(input("Enter number: "))
    print(x / y)
except Exception as e:
    with open("Data/error_log.txt", "a") as log:
        log.write(str(e) + "\n")
    print("Error logged to file")

# Email validation with exception
class InvalidEmailError(Exception):
    pass

try:
    email = input("Enter email: ")
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Invalid email format")
    print("Valid email")
except InvalidEmailError as e:
    print(e)
