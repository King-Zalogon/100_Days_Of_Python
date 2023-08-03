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

# import smtplib
# import base64
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from random_quote import get_random_quote
# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# sender_email = os.getenv('FROM_EMAIL')
# print(sender_email)
# receiver_email = os.getenv('TO_EMAIL')  # Replace with the recipient's email address
# encoded_password = os.getenv('FROM_PASS')  # Get the encoded password from the environment variable
#
#
# if not all([sender_email, receiver_email, encoded_password]):
#     print("One or more environment variables are missing.")
#     exit(1)
#
# # Decode the password back to bytes
# app_password = base64.b64decode(encoded_password.encode('utf-8'))
#
# subject = "Test Email"
# body = get_random_quote()
# email_message = MIMEMultipart()
#
# email_message["From"] = sender_email
# email_message["To"] = receiver_email
# email_message["Subject"] = subject
#
# body_content = MIMEText(body, "plain", "utf-8")  # Encode the body using utf-8
# email_message.attach(body_content)
#
# try:
#     with smtplib.SMTP('smtp.gmail.com', 587) as server:
#         server.ehlo()
#         server.starttls()
#         server.ehlo()
#
#         # Log in to your Gmail account
#         server.login(sender_email, app_password)
#
#         # Send the email
#         server.sendmail(sender_email, receiver_email, email_message.as_string())
#
#     print('Email sent successfully!')
# except smtplib.SMTPAuthenticationError:
#     print("Failed to authenticate. Check your email and app password.")
# except Exception as e:
#     print(f"An error occurred: {e}")
