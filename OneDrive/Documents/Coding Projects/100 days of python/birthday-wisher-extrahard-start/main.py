##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib
import random

# 1. Read the birthdays.csv
birthday_csv = pandas.read_csv("birthdays.csv")

# 2. Get current month/day
current_date = dt.datetime.now().month, dt.datetime.now().day

# 3. Email Credentials
my_email = "pythontestbripor@gmail.com"
password = "likqoxvetxldjuri"

# 4. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv
for index, row in birthday_csv.iterrows():
    birthday = row['month'], row['day']

    if birthday == current_date:
        with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as f:
            letter = f.read()
            b_day_letter = letter.replace('[NAME]', row['name'])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            # make connection secure
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=row['email'],
                                msg=f"Subject:Happy Birthday {row['name']}!\n\n{b_day_letter}"
                                )





