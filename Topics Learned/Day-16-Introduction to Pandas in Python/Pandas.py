# 🐼 Day 16 – Introduction to Pandas
# Author: Mohammad Ali
# Topic: Basics of Pandas (Series & DataFrame)

import pandas as pd

print("---- Creating a Pandas Series ----")

# Creating a Series
sales_series = pd.Series([15000, 23000, 18000, 27000])
print(sales_series)

print("\n---- Creating a DataFrame Manually ----")

# Creating a DataFrame using dictionary
data = {
    "Order_ID": [101, 102, 103, 104],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "Price": [50000, 500, 1500, 12000],
    "Quantity": [2, 5, 3, 1]
}

df = pd.DataFrame(data)

print(df)

print("\n---- Calculating Revenue Column ----")

# Creating a new column
df["Revenue"] = df["Price"] * df["Quantity"]

print(df)

print("\n---- Basic Dataset Information ----")

# Display first few rows
print("\nFirst 3 Rows:")
print(df.head(3))

# Display dataset info
print("\nDataset Info:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())
