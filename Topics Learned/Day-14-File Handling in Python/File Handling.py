# 🐍 Day 14 – File Handling in Python
# Author: Mohammad Ali
# Topic: Reading and Writing Files

print("---- Writing to a File ----")

# Writing data to a file
with open("sales_report.txt", "w") as file:
    file.write("Monthly Sales Report\n")
    file.write("Total Sales: 15000\n")
    file.write("Total Profit: 4500\n")

print("Data written successfully.")

print("\n---- Reading from File ----")

# Reading data from file
with open("sales_report.txt", "r") as file:
    content = file.read()
    print(content)

print("\n---- Appending to File ----")

# Appending additional data
with open("sales_report.txt", "a") as file:
    file.write("New Orders Added: 25\n")

print("New data appended successfully.")
