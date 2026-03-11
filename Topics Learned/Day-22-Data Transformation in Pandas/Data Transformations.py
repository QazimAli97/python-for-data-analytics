# 🐼 Day 22 – Data Transformation in Pandas
# Author: Mohammad Ali
# Topic: Transforming Data using apply(), map(), replace(), rename()

import pandas as pd

print("---- Creating Sales Dataset ----")

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Tablet"],
    "Region": ["N", "S", "E", "W", "N"],
    "Price": [50000, 500, 1500, 12000, 20000],
    "Quantity": [2, 5, 3, 1, 4]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

print("\n---- Creating Revenue Column using apply() ----")

df["Revenue"] = df.apply(lambda row: row["Price"] * row["Quantity"], axis=1)

print(df)

print("\n---- Mapping Region Codes to Names ----")

region_map = {
    "N": "North",
    "S": "South",
    "E": "East",
    "W": "West"
}

df["Region"] = df["Region"].map(region_map)

print(df)

print("\n---- Replacing Product Name ----")

df["Product"] = df["Product"].replace("Mouse", "Wireless Mouse")

print(df)

print("\n---- Renaming Columns ----")

df = df.rename(columns={
    "Price": "Unit_Price",
    "Quantity": "Units_Sold"
})

print(df)
