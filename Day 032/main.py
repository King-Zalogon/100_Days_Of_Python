import smtplib
import datetime as dt
# import random
from random_quote import get_random_quote
import os
from dotenv import load_dotenv



now = dt.datetime.now()
year = now.year
month = now.month  # starts at 1 for January
day_of_the_week = now.weekday()  # starts at 0 for monday
print(day_of_the_week)

birth_date = dt.datetime(year=1990, month=12, day=12, hour=4, minute=30)
print(birth_date)

load_dotenv()
my_email = os.getenv('FROM_EMAIL')
password = os.getenv('FROM_PASS')
receiver_email = os.getenv('TO_EMAIL')

gmail_smtp = 'smtp.gmail.com'
hotmail_smtp = 'smtp.live.com'
outlook_smtp = 'outlook.office365.com'
yahoo_smtp = 'smtp.mail.yahoo.com'


# with open('quotes.txt') as text:
#     quotes_list = text.readlines()

now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 2:
    # today_quote = random.choice(quotes_list)
    today_quote = get_random_quote()
    print(today_quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # to connect to de smtp of the mail
        connection.starttls()  # to encrypt the messages
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_email,
                            msg=f'Subject: Here is your quote!\n\n{today_quote}'
                            )
        connection.close()
    print(day_of_the_week)
    print(today_quote)
