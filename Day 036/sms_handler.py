import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

MY_PHONE = os.getenv('MY_NUMBER')
#print(MY_PHONE)
TWILIO_PHONE = os.getenv('TWI_NUMBER')
#print(TWILIO_PHONE)

account_sid = os.getenv('TWI_ACC_SID')
#print(account_sid)
auth_token = os.getenv("TWI_AUTH_TKN")
#print(auth_token)


def sms_sender(msg_txt):

    client = Client(account_sid, auth_token)
    message = client.messages.create(from_=TWILIO_PHONE, body=msg_txt, to=MY_PHONE)

    return message.status
