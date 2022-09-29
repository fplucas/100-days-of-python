# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / height ** 2)

if(bmi < 18.5):
    description = "you are underweight."
elif(bmi < 25):
    description = "you have a normal weight."
elif(bmi < 30):
    description = "you are slightly overweight."
elif(bmi < 35):
    description = "you are obese."
else:
    description = "you are clinically obese."

print(f"Your BMI is {bmi}, {description}")
