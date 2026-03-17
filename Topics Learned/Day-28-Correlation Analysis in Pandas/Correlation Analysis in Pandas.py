# 🐼 Day 28 – Correlation Analysis in Pandas
# Author: Mohammad Ali
# Topic: Understanding Relationships Between Variables

import pandas as pd

print("---- Creating Sales Dataset ----")

data = {
    "Order_ID": [101, 102, 103, 104, 105, 106],
    "Price": [50000, 500, 1500, 52000, 12000, 550],
    "Quantity": [2, 5, 3, 1, 1, 4],
    "Discount": [5, 10, 8, 6, 7, 12]
}

df = pd.DataFrame(data)

# Create Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

print("\nDataset:")
print(df)

print("\n---- Correlation Matrix ----")

correlation_matrix = df.corr()

print(correlation_matrix)

print("\n---- Correlation with Revenue ----")

print(correlation_matrix["Revenue"])
