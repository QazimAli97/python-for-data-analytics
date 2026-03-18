# 🐼 Day 29 – Mini Project: Sales Data Analysis
# Author: Mohammad Ali
# Topic: End-to-End Data Analysis using Pandas

import pandas as pd

print("---- Creating Sales Dataset ----")

data = {
    "Order_ID": [101, 102, 103, 104, 105, 106, 107],
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Monitor", "Mouse", "Tablet"],
    "Region": ["North", "South", "East", "West", "North", "South", "East"],
    "Price": [50000, 500, 1500, 52000, 12000, 550, 20000],
    "Quantity": [2, 5, 3, 1, 1, 4, 2]
}

df = pd.DataFrame(data)

# Step 1: Create Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

print("\nDataset:")
print(df)

print("\n---- Data Cleaning ----")

# Check missing values
print(df.isnull().sum())

print("\n---- Data Analysis ----")

# Total Revenue
total_revenue = df["Revenue"].sum()
print("Total Revenue:", total_revenue)

# Revenue by Product
product_revenue = df.groupby("Product")["Revenue"].sum()
print("\nRevenue by Product:")
print(product_revenue)

# Revenue by Region
region_revenue = df.groupby("Region")["Revenue"].sum()
print("\nRevenue by Region:")
print(region_revenue)

print("\n---- Top Performing Product ----")

top_product = product_revenue.idxmax()
print("Top Product:", top_product)

print("\n---- Sorting Data ----")

sorted_df = df.sort_values(by="Revenue", ascending=False)
print(sorted_df)
