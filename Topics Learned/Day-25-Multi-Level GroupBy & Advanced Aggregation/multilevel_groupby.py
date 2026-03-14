# 🐼 Day 25 – Multi-Level GroupBy & Advanced Aggregation
# Author: Mohammad Ali
# Topic: Grouping Data by Multiple Columns

import pandas as pd

print("---- Creating Sales Dataset ----")

data = {
    "Order_ID": [101, 102, 103, 104, 105, 106, 107],
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse", "Monitor", "Laptop"],
    "Region": ["North", "South", "East", "West", "North", "South", "East"],
    "Price": [50000, 500, 1500, 52000, 550, 12000, 51000],
    "Quantity": [2, 5, 3, 1, 4, 2, 1]
}

df = pd.DataFrame(data)

# Create Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

print(df)

print("\n---- GroupBy Product and Region ----")

grouped = df.groupby(["Product", "Region"])["Revenue"].sum()

print(grouped)

print("\n---- Multiple Aggregations ----")

summary = df.groupby(["Product", "Region"]).agg({
    "Revenue": "sum",
    "Quantity": "sum",
    "Price": "mean"
})

print(summary)

print("\n---- Resetting Index for Clean Table ----")

summary_reset = summary.reset_index()

print(summary_reset)
