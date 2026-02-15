# 🐍 Day 5 – Lists in Python
# Author: Mohammad Ali
# Topic: Working with Lists (Core Data Structure)

print("---- Creating a List ----")

sales = [1200, 3400, 5600, 2300, 7800]
print("Sales Data:", sales)

print("\n---- Accessing Elements ----")

print("First Sale:", sales[0])
print("Last Sale:", sales[-1])

print("\n---- Updating a Value ----")

sales[1] = 3500
print("Updated Sales Data:", sales)

print("\n---- Adding a New Sale ----")

sales.append(9100)
print("After Adding New Sale:", sales)

print("\n---- Removing a Value ----")

sales.remove(2300)
print("After Removing 2300:", sales)

print("\n---- Looping Through the List ----")

total_sales = 0

for value in sales:
    total_sales += value

print("Total Sales:", total_sales)

average_sales = total_sales / len(sales)
print("Average Sales:", average_sales)
