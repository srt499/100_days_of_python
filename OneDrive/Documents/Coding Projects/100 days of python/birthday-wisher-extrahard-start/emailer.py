import smtplib

def email():
    my_email = "pythontestbripor@gmail.com"
    password = "likqoxvetxldjuri"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        # make connection secure
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivational Quotes\n\n{random.choice(quotes)}"
                            )