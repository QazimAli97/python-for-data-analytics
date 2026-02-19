# 🐍 Day 8 – Tuples in Python
# Author: Mohammad Ali
# Topic: Immutable data structures

print("---- Creating a Tuple ----")

transaction = (101, "2025-01-01", 4500.75)
print("Transaction Record:", transaction)

print("\n---- Accessing Elements ----")

print("Order ID:", transaction[0])
print("Order Date:", transaction[1])
print("Order Amount:", transaction[2])

print("\n---- Looping Through Tuple ----")

for item in transaction:
    print("Value:", item)

print("\n---- Tuple Unpacking ----")

order_id, order_date, order_amount = transaction
print("Unpacked Order ID:", order_id)
print("Unpacked Date:", order_date)
print("Unpacked Amount:", order_amount)

print("\n---- Attempting Modification ----")

print("Tuples are immutable (cannot be modified once created).")
