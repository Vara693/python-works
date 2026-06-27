time = float(input("Enter time(in years): "))*12
amount = float(input("Enter monthly amount: "))
interest = float(input("Enter interest: "))/100/12

money = float(amount*((((1+interest)**time)-1)/interest)*(1+interest))
print(f"The Money after {time} months: ₹",round(money,2))
total_invested = amount * time
profit = money - total_invested

print("Total Invested:", total_invested)
print("Profit:", round(profit, 2))