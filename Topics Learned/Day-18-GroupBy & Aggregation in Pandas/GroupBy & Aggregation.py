# 🐼 Day 18 – GroupBy & Aggregation in Pandas
# Author: Mohammad Ali
# Topic: Summarizing Data using GroupBy

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

# Creating Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

print(df)

print("\n---- Total Revenue by Product ----")

product_revenue = df.groupby("Product")["Revenue"].sum()
print(product_revenue)

print("\n---- Average Price by Product ----")

avg_price = df.groupby("Product")["Price"].mean()
print(avg_price)

print("\n---- Total Quantity Sold by Region ----")

region_sales = df.groupby("Region")["Quantity"].sum()
print(region_sales)

print("\n---- Multiple Aggregations ----")

summary = df.groupby("Product").agg({
    "Revenue": "sum",
    "Quantity": "sum",
    "Price": "mean"
})

print(summary)
