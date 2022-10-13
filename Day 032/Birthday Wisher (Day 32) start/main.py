import smtplib
import datetime as dt
import random
import pandas

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays_dict = data.to_dict(orient='records')
print(birthdays_dict)

now = dt.datetime.now()
month = now.month
day = now.day
today_name = ''
today_email = ''

# 2. Check if today matches a birthday in the birthdays.csv
birthday = False

for i in range(len(birthdays_dict)):
    if birthdays_dict[i]['month'] == month and birthdays_dict[i]['day'] == day:
        today_email = birthdays_dict[i]['email']
        today_name = birthdays_dict[i]['name']
        birthday = True

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv

letters = []
for i in range(1,4):
    with open(f'letter_templates/letter_{i}.txt') as file:
        letters.append(file.read())

print(letters)

template = random.choice(letters)
today_message = template.replace('[NAME]', f'{today_name}')


with open('quotes.txt') as text:
    quotes_list = text.readlines()

# 4. Send the letter generated in step 3 to that person's email address.

my_email = "zalogonking@gmail.com"
password = 'notapassword'

gmail_smtp = 'smtp.gmail.com'
hotmail_smtp = 'smtp.live.com'
yahoo_smtp = 'smtp.mail.yahoo.com'


if birthday:
    today_quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # to connect to de smtp of our mail
        connection.starttls()  # to encrypt the messages
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=today_email,
                            msg=f'Subject: Happy B-day {today_name}!!!\n\n{today_message}\n{today_quote}'
                            )

