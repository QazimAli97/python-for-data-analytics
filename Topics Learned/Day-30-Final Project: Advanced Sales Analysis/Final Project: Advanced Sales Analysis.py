# 🐼 Day 30 – Final Project: Advanced Sales Analysis
# Author: Mohammad Ali
# Topic: End-to-End Data Analysis with Business Insights

import pandas as pd

print("---- Creating Sales Dataset ----")

data = {
    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Monitor", "Mouse", "Tablet", "Laptop"],
    "Region": ["North", "South", "East", "West", "North", "South", "East", "North"],
    "Price": [50000, 500, 1500, 52000, 12000, 550, 20000, 51000],
    "Quantity": [2, 5, 3, 1, 1, 4, 2, 1],
    "Discount": [5, 10, 8, 6, 7, 12, 9, 5]
}

df = pd.DataFrame(data)

# Step 1: Data Cleaning
print("\n---- Checking Missing Values ----")
print(df.isnull().sum())

# Step 2: Feature Engineering
df["Revenue"] = df["Price"] * df["Quantity"]
df["Discounted_Price"] = df["Price"] * (1 - df["Discount"] / 100)

print("\nDataset:")
print(df)

# Step 3: Business Analysis

print("\n---- Total Revenue ----")
print(df["Revenue"].sum())

print("\n---- Revenue by Product ----")
print(df.groupby("Product")["Revenue"].sum())

print("\n---- Revenue by Region ----")
print(df.groupby("Region")["Revenue"].sum())

print("\n---- Average Discount by Product ----")
print(df.groupby("Product")["Discount"].mean())

print("\n---- Top Performing Product ----")
print(df.groupby("Product")["Revenue"].sum().idxmax())

print("\n---- Top Region ----")
print(df.groupby("Region")["Revenue"].sum().idxmax())

print("\n---- Sorted Data (Top Revenue) ----")
print(df.sort_values(by="Revenue", ascending=False))
