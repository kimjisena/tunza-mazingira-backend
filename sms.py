import africastalking
import os
import re
from datetime import datetime

# Initialize cache
cache_responses = [
    {
        "SMSMessageData": {
            "Message": 'Sent to 1/2 Total Cost: TZS 22.0000',
            "Recipients": [["Object"]]
        }
    },
    {
        "SMSMessageData": {
            "Message": 'Sent to 4/5 Total Cost: TZS 22.0000',
            "Recipients": [["Object"]]
        }
    }
]

# Initialize Africa's Talking
username = 'rahma'
api_key = 'bb882af712e3beb16bfb749914d0a5c69395704433a5848804b923891536693b'

africastalking.initialize(username, api_key)


def print_env():
    print(f'username: {username}')
    print(f'api_key: {api_key}')


class SendSMS():
    sms = africastalking.SMS

    def sending(self):
        # Set the numbers in international format
        recipients = ["+255674992189",]

        # Set your message
        message = "Karibu! Gari la kusafisha mji litawasili kesho. Tuko tayari kudumisha usafi na uzuri wa mji wetu. Asante kwa ushirikiano wako!\n#UsafiWaMji"

        # Set your shortCode or senderId
        # sender = "AFRICASTKNG"

        try:
            response = self.sms.send(message, recipients)
            print(response)
            cache_responses[datetime.now().strftime(
                "%d/%m/%Y")] = sent_number(response["Message"])
            # sample response
            # {
            #     SMSMessageData: {
            #     Message: 'Sent to 1/1 Total Cost: TZS 22.0000',
            #     Recipients: [ [Object] ]
            #     }
            # }
        except Exception as e:
            print(f'Tenemos una problema: {e}')


def sent_number(message: str):
    # input_string = "Sent to 1/1 Total Cost: TZS 22.0000"

    match = re.search(r"Sent to (\d+/\d+)", message)

    if match:
        matched = match.group(1).split("/")
        return {
            "sent": matched[1],
            "received": matched[0]
        }
    else:
        print("None")
