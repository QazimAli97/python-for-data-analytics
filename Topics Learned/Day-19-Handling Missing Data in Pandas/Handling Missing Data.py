# 🐼 Day 19 – Handling Missing Data in Pandas
# Author: Mohammad Ali
# Topic: Detecting and Handling Missing Values

import pandas as pd
import numpy as np

print("---- Creating Dataset with Missing Values ----")

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Tablet"],
    "Price": [50000, 500, None, 12000, 20000],
    "Quantity": [2, None, 3, 1, 4]
}

df = pd.DataFrame(data)

print(df)

print("\n---- Detecting Missing Values ----")

print(df.isnull())

print("\n---- Counting Missing Values ----")

print(df.isnull().sum())

print("\n---- Filling Missing Values ----")

# Fill missing values
df["Price"].fillna(df["Price"].mean(), inplace=True)
df["Quantity"].fillna(0, inplace=True)

print(df)

print("\n---- Dropping Missing Values ----")

cleaned_df = df.dropna()

print(cleaned_df)
