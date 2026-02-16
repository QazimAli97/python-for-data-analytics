# 🐍 Day 6 – Dictionaries in Python
# Author: Mohammad Ali
# Topic: Working with key-value data structures

print("---- Creating a Dictionary ----")

customer = {
    "name": "Ali",
    "region": "West",
    "total_sales": 8500,
    "profit": 1200
}

print("Customer Data:", customer)

print("\n---- Accessing Values ----")

print("Customer Name:", customer["name"])
print("Customer Region:", customer["region"])

print("\n---- Updating Values ----")

customer["total_sales"] = 9000
print("Updated Sales:", customer["total_sales"])

print("\n---- Adding New Key-Value Pair ----")

customer["status"] = "Gold"
print("Updated Customer Record:", customer)

print("\n---- Removing a Key ----")

customer.pop("status")
print("After Removing Status:", customer)

print("\n---- Looping Through Dictionary ----")

for key, value in customer.items():
    print(key, ":", value)
