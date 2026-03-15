# 🐼 Day 26 – Exporting Data using Pandas
# Author: Mohammad Ali
# Topic: Saving Processed Data to CSV and Excel

import pandas as pd

print("---- Creating Sales Dataset ----")

data = {
    "Order_ID": [101, 102, 103, 104, 105],
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Tablet"],
    "Region": ["North", "South", "East", "West", "North"],
    "Price": [50000, 500, 1500, 12000, 20000],
    "Quantity": [2, 5, 3, 1, 4]
}

df = pd.DataFrame(data)

# Creating Revenue column
df["Revenue"] = df["Price"] * df["Quantity"]

print(df)

print("\n---- Exporting Data to CSV ----")

df.to_csv("sales_report.csv", index=False)

print("CSV file saved successfully.")

print("\n---- Exporting Data to Excel ----")

df.to_excel("sales_report.xlsx", index=False)

print("Excel file saved successfully.")
