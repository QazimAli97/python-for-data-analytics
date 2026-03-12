# 🐼 Day 23 – Merging & Joining Data in Pandas
# Author: Mohammad Ali
# Topic: Combining Datasets using merge()

import pandas as pd

print("---- Creating Orders Dataset ----")

orders = {
    "Order_ID": [101, 102, 103, 104],
    "Customer_ID": [1, 2, 3, 1],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"]
}

orders_df = pd.DataFrame(orders)

print(orders_df)

print("\n---- Creating Customers Dataset ----")

customers = {
    "Customer_ID": [1, 2, 3],
    "Customer_Name": ["Ali", "Sara", "John"],
    "Region": ["North", "South", "West"]
}

customers_df = pd.DataFrame(customers)

print(customers_df)

print("\n---- Merging Datasets (INNER JOIN) ----")

merged_df = pd.merge(orders_df, customers_df, on="Customer_ID", how="inner")

print(merged_df)

print("\n---- LEFT JOIN Example ----")

left_join = pd.merge(orders_df, customers_df, on="Customer_ID", how="left")

print(left_join)
