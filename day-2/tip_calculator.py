print("Welcome to the tip calculator.")
gross_total = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
number_of_people = int(input("How many people to split the bill?"))

net_total = gross_total + (gross_total / 100 * percentage_tip)
pay_per_person = net_total / number_of_people

print(f"Each person should pay: ${pay_per_person:.2f}")
