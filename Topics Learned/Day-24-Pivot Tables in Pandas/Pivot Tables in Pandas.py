# 🐼 Day 24 – Pivot Tables in Pandas
# Author: Mohammad Ali
# Topic: Creating Pivot Tables for Data Analysis

import pandas as pd

print("---- Creating Sales Dataset ----")

data = {
    "Order_ID": [101, 102, 103, 104, 105, 106],
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse", "Monitor"],
    "Region": ["North", "South", "East", "West", "North", "South"],
    "Price": [50000, 500, 1500, 52000, 550, 12000],
    "Quantity": [2, 5, 3, 1, 4, 2]
}

df = pd.DataFrame(data)

# Create Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

print(df)

print("\n---- Pivot Table: Revenue by Product ----")

pivot_product = pd.pivot_table(
    df,
    values="Revenue",
    index="Product",
    aggfunc="sum"
)

print(pivot_product)

print("\n---- Pivot Table: Revenue by Region and Product ----")

pivot_region_product = pd.pivot_table(
    df,
    values="Revenue",
    index="Region",
    columns="Product",
    aggfunc="sum",
    fill_value=0
)

print(pivot_region_product)
