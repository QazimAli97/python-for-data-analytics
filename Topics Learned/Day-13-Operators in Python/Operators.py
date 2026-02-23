# 🐍 Day 13 – Operators in Python
# Author: Mohammad Ali
# Topic: Arithmetic, Comparison, Logical Operators

print("---- Arithmetic Operators ----")

revenue = 10000
cost = 7500

profit = revenue - cost
margin = profit / revenue

print("Profit:", profit)
print("Profit Margin:", margin)

print("\n---- Comparison Operators ----")

if profit > 0:
    print("Profitable Business")

if margin >= 0.20:
    print("Healthy Margin")

print("\n---- Logical Operators ----")

sales = 8000
region = "West"

if sales > 5000 and region == "West":
    print("Strong Regional Performance")

print("\n---- Assignment Operators ----")

bonus = 1000
bonus += 500   # equivalent to bonus = bonus + 500
print("Updated Bonus:", bonus)

print("\n---- Modulus Operator ----")

orders = 15

if orders % 2 == 0:
    print("Even number of orders")
else:
    print("Odd number of orders")
