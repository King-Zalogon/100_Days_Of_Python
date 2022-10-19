import os
from twilio.rest import Client

MY_PHONE = "some phone number"
TWILIO_PHONE = "+13608001966"

account_sid = os.environ.get('TWILIO_ACC_SID')
auth_token = os.environ.get("TWILIO_AUTH_TKN")


def sms_sender(msg_txt):

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=msg_txt,
        from_=TWILIO_PHONE,
        to=MY_PHONE
    )

    return message.status
