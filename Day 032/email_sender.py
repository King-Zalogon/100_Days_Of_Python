import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from random_quote import get_random_quote
import os
from dotenv import load_dotenv

load_dotenv()


sender_email = os.getenv('FROM_EMAIL')
receiver_email = os.getenv('TO_EMAIL')  # Replace with the recipient's email address
app_password = os.getenv('FROM_PASS')  # Replace with your generated app password

subject = "Test Email"
body = get_random_quote()
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

try:
    # Create an SMTP instance with debug output

    print('starting...')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:

        print('started')
        server.set_debuglevel(1)

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
