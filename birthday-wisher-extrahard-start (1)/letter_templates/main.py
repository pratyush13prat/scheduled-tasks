##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
import random
import datetime as dt
import pandas

rn = dt.datetime.now()
month = rn.month
day = rn.day

# Load CSV
df = pandas.read_csv("birthdays.csv")

# Store letters
letters = []

with open("letter_1.txt", "r") as file1:
    letters.append(file1.read())

with open("letter_2.txt", "r") as file2:
    letters.append(file2.read())

with open("letter_3.txt", "r") as file3:
    letters.append(file3.read())

# Check birthdays
for index, row in df.iterrows():
    if row["month"] == month and row["day"] == day:
        chosen_letter = random.choice(letters)
        print("Birthday found!")
        namess = row["name"]
        chosen_letter = chosen_letter.replace("NAME", namess)
        print(chosen_letter)
# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
import os
mymail = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")
to_addrs = os.environ.get("TO_ADDRS")
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=mymail, password=password)
    connection.sendmail(from_addr=mymail, to_addrs=to_addrs, msg=f"Subject:Happy Birthday!\n\n{chosen_letter}")

