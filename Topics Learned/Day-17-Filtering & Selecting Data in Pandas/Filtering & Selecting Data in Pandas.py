# 🐼 Day 17 – Filtering & Selecting Data in Pandas
# Author: Mohammad Ali
# Topic: Data Selection and Filtering

import pandas as pd

print("---- Creating Sales Dataset ----")

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Tablet"],
    "Price": [50000, 500, 1500, 12000, 20000],
    "Quantity": [2, 5, 3, 1, 4]
}

df = pd.DataFrame(data)

# Creating Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

print(df)

print("\n---- Selecting Specific Columns ----")

# Selecting single column
print("\nProduct Column:")
print(df["Product"])

# Selecting multiple columns
print("\nProduct and Revenue Columns:")
print(df[["Product", "Revenue"]])

print("\n---- Filtering Data ----")

# Filter: Revenue greater than 30000
high_revenue = df[df["Revenue"] > 30000]
print("\nOrders with Revenue > 30000:")
print(high_revenue)

# Filter: Quantity greater than 3
high_quantity = df[df["Quantity"] > 3]
print("\nOrders with Quantity > 3:")
print(high_quantity)

print("\n---- Multiple Conditions Filtering ----")

# Revenue > 30000 AND Quantity > 1
filtered_data = df[(df["Revenue"] > 30000) & (df["Quantity"] > 1)]
print(filtered_data)
