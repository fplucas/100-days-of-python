# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age = int(age)
years_to_90 = 90 - age
days_left = years_to_90 * 365
weeks_left = years_to_90 * 52
months_left = years_to_90 * 12

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
