income = int(input("Enter your monthly income: "))
expense = int(input("Enter your total monthly expense: "))
Monthly_savings = income - expense
Projectedsavings = Monthly_savings * 12 + (Monthly_savings* 12 * 0.05)
print(f"Your monthly savings are ${Monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${Projectedsavings}")