# 🐼 Day 21 – Data Cleaning: Removing Duplicates
# Author: Mohammad Ali
# Topic: Handling Duplicate Data

import pandas as pd

print("---- Creating Dataset with Duplicates ----")

data = {
    "Order_ID": [101, 102, 103, 103, 104, 105],
    "Product": ["Laptop", "Mouse", "Keyboard", "Keyboard", "Monitor", "Tablet"],
    "Price": [50000, 500, 1500, 1500, 12000, 20000],
    "Quantity": [2, 5, 3, 3, 1, 4]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

print("\n---- Detecting Duplicate Rows ----")

duplicates = df.duplicated()
print(duplicates)

print("\n---- Counting Duplicate Rows ----")

print("Total duplicates:", duplicates.sum())

print("\n---- Removing Duplicate Rows ----")

clean_df = df.drop_duplicates()

print("\nCleaned Dataset:")
print(clean_df)
