import smtplib
import datetime as dt
import random
import pandas

MY_EMAIL = "zalogonking@gmail.com"
PASSWORD = 'not a password'

data = pandas.read_csv("birthdays.csv")
birthdays_dict = data.to_dict(orient='records')

month = dt.datetime.now().month
day = dt.datetime.now().day

today_name = ''
today_email = ''
birthday = False
letters = []

for i in range(1, 4):
    with open(f'letter_templates/letter_{i}.txt') as file:
        letters.append(file.read())

template = random.choice(letters)
today_message = template.replace('[NAME]', f'{today_name}')

with open('quotes.txt') as text:
    quotes_list = text.readlines()

for i in range(len(birthdays_dict)):
    if birthdays_dict[i]['month'] == month and birthdays_dict[i]['day'] == day:
        today_email = birthdays_dict[i]['email']
        today_name = birthdays_dict[i]['name']
        birthday = True

if birthday:
    today_quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # to connect to de smtp of our mail
        connection.starttls()  # to encrypt the messages
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=today_email,
                            msg=f'Subject: Happy B-day {today_name}!!!\n\n{today_message}\n{today_quote}'
                            )
