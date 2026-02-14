# 🐍 Day 4 – Loops in Python
# Author: Mohammad Ali
# Topic: Automating repetitive tasks using loops

print("---- For Loop Example ----")

# Example 1: Printing numbers
for i in range(1, 6):
    print("Number:", i)


print("\n---- Sales Data Analysis ----")

sales = [1200, 3400, 5600, 2300, 7800]

total_sales = 0

for value in sales:
    total_sales += value

print("Total Sales:", total_sales)


print("\n---- Profit Classification ----")

profits = [200, -150, 300, -50, 400]

for profit in profits:
    if profit > 0:
        print("Profitable Transaction:", profit)
    else:
        print("Loss Transaction:", profit)


print("\n---- While Loop Example ----")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1
