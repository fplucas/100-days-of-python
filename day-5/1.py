# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

heights_sumup = 0
counter = 0
for height in student_heights:
    heights_sumup += height
    counter += 1

average = round(heights_sumup / counter)
print(average)

