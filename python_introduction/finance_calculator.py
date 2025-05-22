# User Input for Financial Details:

# Prompt the user for their monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings:
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings:
# Using the formula: Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)
annual_savings = monthly_savings * 12
interest_earned = annual_savings * 0.05
projected_savings = annual_savings + interest_earned

# Output Results:
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")