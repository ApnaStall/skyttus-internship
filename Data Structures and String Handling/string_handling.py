# -------------------------
# Python String Handling
# -------------------------

# Take a string input and print its length
text = input("Enter a string: ")
print("Length:", len(text))

# Convert a sentence to lowercase
sentence = input("Enter a sentence: ")
print("Lowercase:", sentence.lower())

# Replace spaces with underscores
string_with_spaces = input("Enter a string: ")
print("With underscores:", string_with_spaces.replace(" ", "_"))

# Extract first and last character
word = input("Enter a word: ")
print("First character:", word[0])
print("Last character:", word[-1])

# Reverse a string using slicing
original = input("Enter a string to reverse: ")
print("Reversed:", original[::-1])

# Count how many times a letter appears
main_string = input("Enter a string: ")
letter = input("Enter a letter to count: ")
print("Count:", main_string.count(letter))

# Check if a word is present in a sentence
sentence = input("Enter a sentence: ")
word = input("Enter a word to search: ")
print("Present:", word in sentence)

# Take name & age and print using f-string
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old.")

# Remove extra spaces from start and end
extra_space_string = input("Enter string with extra spaces: ")
print("Trimmed:", extra_space_string.strip())

# Join list of words with hyphen
words = ["Python", "AI", "ML", "Internship"]
print("Joined string:", "-".join(words))


# -------------------------
# Python List Operations
# -------------------------

# Create a list of 5 favorite movies
movies = ["Inception", "Interstellar", "Matrix", "Avatar", "Titanic"]
print("Movies:", movies)

# Add a new movie
movies.append("Gladiator")
print("After adding:", movies)

# Remove the first movie
movies.pop(0)
print("After removing first:", movies)

# Sort a list of numbers
numbers = [45, 12, 89, 34, 7]
numbers.sort()
print("Sorted list:", numbers)

# Reverse a list
numbers.reverse()
print("Reversed list:", numbers)

# Find the largest number
print("Largest number:", max(numbers))

# Merge two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print("Merged list:", merged_list)

# Access last element without index number
print("Last element:", merged_list[-1])

# Nested list and access inner element
nested_list = [[1, 2], [3, 4], [5, 6]]
print("Inner element:", nested_list[1][1])

# Count occurrences of an element in a list
sample_list = [1, 2, 3, 2, 4, 2, 5]
print("Count of 2:", sample_list.count(2))
