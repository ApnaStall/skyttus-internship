# Read a file and display contents
with open("Data/sample.txt", "r") as file:
    print(file.read())

# Count number of lines in a file
with open("Data/sample.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

# Count word frequency in a file
with open("Data/sample.txt", "r") as file:
    text = file.read().lower()
    words = text.split()
    word_count = {}

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

print("Word frequency:", word_count)

# Write 5 user-entered sentences to a file
with open("Data/sentences.txt", "w") as file:
    for i in range(5):
        sentence = input(f"Enter sentence {i + 1}: ")
        file.write(sentence + "\n")

print("Sentences written to file")

# Append list of strings to an existing file
lines_to_add = ["Python\n", "AI\n", "ML\n"]
with open("Data/sentences.txt", "a") as file:
    file.writelines(lines_to_add)

print("List appended to file")

# Print lines containing a specific word
search_word = input("Enter word to search: ")
with open("Data/sample.txt", "r") as file:
    for line in file:
        if search_word in line:
            print(line.strip())

# Replace a word in a file and save changes
with open("Data/sample.txt", "r") as file:
    content = file.read()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

content = content.replace(old_word, new_word)

with open("Data/sample.txt", "w") as file:
    file.write(content)

print("Word replaced successfully")

# Merge two files into a third file
with open("Data/file1.txt", "r") as f1, open("Data/file2.txt", "r") as f2:
    content1 = f1.read()
    content2 = f2.read()

with open("Data/merged.txt", "w") as merged:
    merged.write(content1 + "\n" + content2)

print("Files merged successfully")

# Read CSV file and display formatted content
with open("Data/data.csv", "r") as file:
    for line in file:
        values = line.strip().split(",")
        print(" | ".join(values))

# Backup a file
with open("Data/sample.txt", "r") as original:
    content = original.read()

with open("Data/backup_sample.txt", "w") as backup:
    backup.write(content)

print("Backup created successfully")
