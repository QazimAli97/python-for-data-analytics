# 🐍 Day 12 – Exception Handling
# Author: Mohammad Ali
# Topic: Writing safer code using try-except

print("---- Basic Exception Handling ----")

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numeric input.")

else:
    print("Calculation successful.")

finally:
    print("Execution completed.")


print("\n---- Business Example ----")

profits = [500, 300, 0, -200]

try:
    average_profit = sum(profits) / len(profits)
    print("Average Profit:", average_profit)

except Exception as e:
    print("Unexpected error:", e)
