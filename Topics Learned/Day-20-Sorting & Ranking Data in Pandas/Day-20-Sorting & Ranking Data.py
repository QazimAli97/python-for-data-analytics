# 🐼 Day 20 – Sorting & Ranking Data in Pandas
# Author: Mohammad Ali
# Topic: Sorting and Ranking Data

import pandas as pd

print("---- Creating Sales Dataset ----")

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Tablet"],
    "Price": [50000, 500, 1500, 12000, 20000],
    "Quantity": [2, 5, 3, 1, 4]
}

df = pd.DataFrame(data)

# Create Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

print(df)

print("\n---- Sorting by Revenue (Highest First) ----")

sorted_df = df.sort_values(by="Revenue", ascending=False)
print(sorted_df)

print("\n---- Sorting by Quantity ----")

quantity_sorted = df.sort_values(by="Quantity")
print(quantity_sorted)

print("\n---- Ranking Products by Revenue ----")

df["Revenue_Rank"] = df["Revenue"].rank(ascending=False)

print(df)
