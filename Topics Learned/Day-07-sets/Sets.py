# 🐍 Day 7 – Sets in Python
# Author: Mohammad Ali
# Topic: Working with unique data collections

print("---- Creating a Set ----")

customers = {"Ali", "Ahmed", "Sara", "Ali"}
print("Customer Set (Duplicates Removed):", customers)

print("\n---- Adding an Element ----")

customers.add("Zara")
print("After Adding Zara:", customers)

print("\n---- Removing an Element ----")

customers.remove("Ahmed")
print("After Removing Ahmed:", customers)

print("\n---- Set Operations ----")

product_a_customers = {"Ali", "Sara", "Zara"}
product_b_customers = {"Sara", "Zara", "Omar"}

print("Product A Customers:", product_a_customers)
print("Product B Customers:", product_b_customers)

# Union
print("\nUnion:", product_a_customers.union(product_b_customers))

# Intersection
print("Intersection:", product_a_customers.intersection(product_b_customers))

# Difference
print("Difference (A - B):", product_a_customers.difference(product_b_customers))
