# 🐍 Day 3 – Conditional Logic (If / Else)
# Author: Mohammad Ali

print("---- Sales & Profit Evaluation ----")

sales = 7500
profit = 1200

# Check sales performance
if sales > 5000:
    print("High Sales Order")
else:
    print("Low Sales Order")

# Check profitability
if profit > 0:
    print("Profitable Transaction")
else:
    print("Loss-Making Transaction")


print("\n---- Customer Segmentation ----")

customer_revenue = 8200

if customer_revenue >= 10000:
    print("Customer Tier: Platinum")
elif customer_revenue >= 5000:
    print("Customer Tier: Gold")
else:
    print("Customer Tier: Silver")


print("\n---- Risk Detection ----")

order_value = 300
minimum_required = 500

if order_value < minimum_required:
    print("Alert: Low-Value Order")
else:
    print("Order Value Acceptable")
