weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆


# Write your code 👇 below:

def celsius_to_fahrenheit(temp_c):
    return (temp_c * 9 / 5) + 32


weather_f = {day_of_the_week: celsius_to_fahrenheit(
    temp_c) for (day_of_the_week, temp_c) in weather_c.items()}

print(weather_f)
