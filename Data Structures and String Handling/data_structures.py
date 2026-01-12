# -------------------------
# Tuple Operations
# -------------------------

# Create a tuple with 5 numbers
numbers_tuple = (10, 20, 30, 40, 50)
print("Tuple:", numbers_tuple)

# Access the third element
print("Third element:", numbers_tuple[2])

# Unpack tuple into variables
a, b, c, d, e = numbers_tuple
print("Unpacked values:", a, b, c, d, e)


# -------------------------
# Set Operations
# -------------------------

# Create a set of 5 fruits
fruits = {"apple", "banana", "mango", "orange", "grape"}
print("Fruits set:", fruits)

# Add a new fruit
fruits.add("pineapple")
print("After adding:", fruits)

# Remove an element from the set
fruits.remove("banana")
print("After removing:", fruits)

# Union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)

# Intersection of two sets
print("Intersection:", set1 & set2)

# Check subset
print("Is subset:", {1, 2}.issubset(set1))

# Remove duplicates using set
duplicate_list = [1, 2, 2, 3, 4, 4, 5]
unique_values = set(duplicate_list)
print("Unique values:", unique_values)


# -------------------------
# Dictionary Operations
# -------------------------

# Create a dictionary of student names and marks
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print("Students:", students)

# Add a new key-value pair
students["David"] = 88
print("After adding:", students)

# Delete a key-value pair
del students["Charlie"]
print("After deletion:", students)

# Merge two dictionaries
extra_students = {"Eve": 92, "Frank": 80}
merged_dict = students | extra_students
print("Merged dictionary:", merged_dict)

# Check if a key exists
print("Bob exists:", "Bob" in merged_dict)

# Count word frequency in a string
sentence = "python is easy and python is powerful"
words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word frequency:", word_count)

# Find key with maximum value
print("Top scorer:", max(merged_dict, key=merged_dict.get))

# Reverse keys and values
reversed_dict = {value: key for key, value in merged_dict.items()}
print("Reversed dictionary:", reversed_dict)

# Update value for a specific key
merged_dict["Bob"] = 95
print("Updated marks:", merged_dict)

# Convert list of tuples to dictionary
tuple_list = [("Math", 90), ("Science", 85), ("English", 88)]
marks_dict = dict(tuple_list)
print("Dictionary from tuples:", marks_dict)
