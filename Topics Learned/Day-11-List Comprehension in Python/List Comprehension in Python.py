# 🐍 Day 11 – List Comprehension
# Author: Mohammad Ali
# Topic: Writing cleaner and efficient loops

print("---- Basic List Comprehension ----")

numbers = [1, 2, 3, 4, 5]

# Traditional loop
squares = []
for num in numbers:
    squares.append(num * num)

print("Squares (Traditional Loop):", squares)

# List comprehension
squares_comp = [num * num for num in numbers]
print("Squares (List Comprehension):", squares_comp)


print("\n---- Conditional List Comprehension ----")

profits = [500, -200, 300, -100, 700]

# Filter profitable transactions
profitable = [value for value in profits if value > 0]
print("Profitable Transactions:", profitable)


print("\n---- Business Example ----")

sales = [1000, 2000, 3000, 4000]

# Increase sales by 10%
updated_sales = [value * 1.10 for value in sales]
print("Updated Sales (10% Increase):", updated_sales)
