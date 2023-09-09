import requests
import smtplib
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

TARGET_PRICE = 300.0

sender_email = os.getenv('FROM_EMAIL')
receiver_email = os.getenv('TO_EMAIL')  # Replace with the recipient's email address
app_password = os.getenv('FROM_PASS')  # Replace with your generated app password

# URL of the product page
item_url = 'https://www.amazon.com/Oculus-Quest-Advanced-All-One-Virtual/dp/B099VMT8VZ/'
# item_url = 'https://www.amazon.com/Valve-Release-Headset-Stations-Controllers/dp/B07VPRVBFF/ref=sr_1_6'

my_headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept-Language':
    'en-US,en;q=0.5',
}

# Send a request to the URL
response = requests.get(url=item_url, headers=my_headers)
if response.status_code != 200:
    print("Error status code: " + str(response.status_code))

# Create a beautiful soup object
soup = BeautifulSoup(response.content, 'lxml')

item_title = soup.find(id="productTitle").get_text().strip()
print(item_title)

# Find the price element
item_price_string = soup.find(class_="a-price-whole").get_text().strip('$')


# Extract the price
foo = list(item_price_string)
bar = []

for char in foo:
    if char != ',':
        bar.append(char)

item_price = float("".join(bar))


if item_price < TARGET_PRICE:

    subject = f"{item_title} price is low!"
    body = f"{item_title} is now available for ${item_price}!"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        # Create an SMTP instance with debug output

        print('starting...')
        with smtplib.SMTP("smtp.gmail.com", port=587) as server:

            print('started')
            # server.set_debuglevel(1)

            # Log in to your Gmail account
            print('logging...')
            server.login(sender_email, app_password)
            print('logged in')

            # Create the email message
            message = f'Subject: {subject}\n\n{body}'

            # Send the email
            print('sending message...')
            server.sendmail(sender_email, receiver_email, message)

        print('Email sent successfully!')
    except smtplib.SMTPAuthenticationError:
        print("Failed to authenticate. Check your email and app password.")
    except Exception as e:
        print(f"An error occurred: {e}")
