yearly_salary = float(input(" Enter your yearly salary: "))
portion_saved= float(input(" Enter the percent of your salary to save, as a decimal:  "))
cost_of_dream_home = float(input(" Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = 0.25
r = 0.05
amount_saved = 0.0
months = 0

down_payment_needed = cost_of_dream_home * portion_down_payment


while amount_saved < down_payment_needed:
    investment_return = amount_saved * (r / 12)
    monthly_saved = (yearly_salary / 12) * portion_saved
    amount_saved += monthly_saved + investment_return
    months += 1

    if months % 6 == 0:
        yearly_salary += yearly_salary * semi_annual_raise

print("Number of months:", months)