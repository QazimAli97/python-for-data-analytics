# 🐍 Day 15 – Working with CSV Files in Python
# Author: Mohammad Ali
# Topic: Reading and Processing CSV Data

import csv

print("---- Creating CSV File ----")

# Writing data to CSV file
with open("sales_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    # Writing header
    writer.writerow(["Order_ID", "Product", "Price", "Quantity"])
    
    # Writing rows
    writer.writerow([101, "Laptop", 50000, 2])
    writer.writerow([102, "Mouse", 500, 5])
    writer.writerow([103, "Keyboard", 1500, 3])

print("CSV file created successfully.")

print("\n---- Reading and Processing CSV File ----")

total_revenue = 0

# Reading CSV file
with open("sales_data.csv", "r") as file:
    reader = csv.reader(file)
    
    header = next(reader)  # Skip header
    print("Header:", header)
    
    for row in reader:
        order_id = int(row[0])
        product = row[1]
        price = int(row[2])
        quantity = int(row[3])
        
        revenue = price * quantity
        total_revenue += revenue
        
        print(f"Order {order_id} | Product: {product} | Revenue: {revenue}")

print("\nTotal Revenue:", total_revenue)

print("\n---- Appending New Order ----")

# Appending new data
with open("sales_data.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([104, "Monitor", 12000, 1])

print("New order appended successfully.")
