##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

import smtplib
import datetime as dt
import pandas
import random
from my_email import EMAIL

NUMBER_OF_LETTERS_AVAILABLE = 3

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("day-32/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"])                  : data_row for (index, data_row) in data.iterrows()}
# # 2. Check if today matches a birthday in the birthdays.csv
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    letter_file_path = f'day-32/letter_templates/letter_{random.randint(1, NUMBER_OF_LETTERS_AVAILABLE)}.txt'
    # # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(letter_file_path) as f:
        letter = f.read()
        custom_letter = letter.replace("[NAME]", birthday_person["name"])

# # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP(EMAIL["smtp_server"], 587) as connection:
            connection.starttls()
            connection.login(EMAIL["username"], EMAIL["password"])
            connection.sendmail(
                from_addr=EMAIL["username"], to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday\n\n{custom_letter}")
