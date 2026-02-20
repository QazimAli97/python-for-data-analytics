# 🐍 Day 10 – Lambda, map(), filter()
# Author: Mohammad Ali
# Topic: Functional programming basics

print("---- Lambda Function Example ----")

# Normal function
def square(x):
    return x * x

print("Square (Normal Function):", square(5))

# Lambda equivalent
square_lambda = lambda x: x * x
print("Square (Lambda):", square_lambda(5))


print("\n---- Using map() ----")

sales = [1000, 2000, 3000, 4000]

# Increase sales by 10%
updated_sales = list(map(lambda x: x * 1.10, sales))
print("Original Sales:", sales)
print("Updated Sales (10% Increase):", updated_sales)


print("\n---- Using filter() ----")

profits = [500, -200, 300, -100, 700]

# Filter only profitable transactions
profitable = list(filter(lambda x: x > 0, profits))
print("All Profits:", profits)
print("Profitable Transactions:", profitable)


print("\n---- Combined Business Example ----")

revenues = [12000, 7000, 3000, 15000]

# Filter high-value customers (>= 10000)
high_value = list(filter(lambda x: x >= 10000, revenues))
print("High Value Customers:", high_value)
