# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

first_digit = 0
second_digit = 0

both_names = (name1 + name2).lower()

for letter in "true":
    first_digit += both_names.count(letter)

for letter in "love":
    second_digit += both_names.count(letter)

love_score = int(str(first_digit) + str(second_digit))

if(love_score < 10 or love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif(40 <= love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

