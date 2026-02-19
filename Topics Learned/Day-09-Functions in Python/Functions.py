# 🐍 Day 9 – Functions in Python
# Author: Mohammad Ali
# Topic: Creating reusable logic using functions

print("---- Defining a Function ----")

def greet(name):
    print("Hello,", name)

greet("Mohammad")

print("\n---- Function with Return Value ----")

def calculate_profit(revenue, cost):
    profit = revenue - cost
    return profit

result = calculate_profit(10000, 7500)
print("Profit:", result)

print("\n---- Function for Customer Tier Classification ----")

def customer_tier(revenue):
    if revenue >= 10000:
        return "Platinum"
    elif revenue >= 5000:
        return "Gold"
    else:
        return "Silver"

tier = customer_tier(8200)
print("Customer Tier:", tier)

print("\n---- Reusing Function ----")

revenues = [12000, 7000, 3000]

for value in revenues:
    print("Revenue:", value, "→ Tier:", customer_tier(value))
