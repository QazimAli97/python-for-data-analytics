# 🐼 Day 27 – Basic Exploratory Data Analysis (EDA)
# Author: Mohammad Ali
# Topic: Exploring Dataset using Pandas

import pandas as pd

print("---- Creating Sales Dataset ----")

data = {
    "Order_ID": [101, 102, 103, 104, 105, 106],
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Monitor", "Mouse"],
    "Region": ["North", "South", "East", "West", "North", "South"],
    "Price": [50000, 500, 1500, 52000, 12000, 550],
    "Quantity": [2, 5, 3, 1, 1, 4]
}

df = pd.DataFrame(data)

# Create Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

print("\nDataset:")
print(df)

print("\n---- Dataset Shape ----")
print(df.shape)

print("\n---- Dataset Columns ----")
print(df.columns)

print("\n---- Dataset Information ----")
print(df.info())

print("\n---- Statistical Summary ----")
print(df.describe())

print("\n---- Unique Product Count ----")
print(df["Product"].value_counts())

print("\n---- Average Revenue ----")
print(df["Revenue"].mean())
