# 🐍 Day 2 – Strings in Python
# Author: Mohammad Ali
# Topic: String operations and text handling

print("---- Basic String Operations ----")

name = "Mohammad Ali"
profession = "Data Analyst"

# Concatenation
print("Hello, my name is " + name + " and I am a " + profession)

# Case conversion
print("\nUppercase Name:", name.upper())
print("Lowercase Profession:", profession.lower())
print("Title Case Profession:", profession.title())

# Length of string
print("\nLength of Name:", len(name))

print("\n---- Text Cleaning ----")

text = "   Python for Data Analytics   "
print("Before Strip:", text)
print("After Strip:", text.strip())

# Replace text
updated_profession = profession.replace("Data", "Business")
print("\nUpdated Profession:", updated_profession)

print("\n---- Searching in Strings ----")

sentence = "I am learning Python for analytics"
print("Is 'Python' in sentence?", "Python" in sentence)

print("\n---- Indexing & Slicing ----")

word = "Analytics"
print("First Letter:", word[0])
print("Last Letter:", word[-1])
print("First 4 Letters:", word[:4])
