from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

TWILIO_VERIFIED_NUMBER = os.getenv('MY_NUMBER')
TWILIO_VIRTUAL_NUMBER = os.getenv('TWI_NUMBER')
TWILIO_SID = os.getenv('TWI_ACC_SID')
TWILIO_AUTH_TOKEN = os.getenv("TWI_AUTH_TKN")


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
