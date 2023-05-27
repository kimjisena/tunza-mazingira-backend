import africastalking
import os
import re
from datetime import datetime

# Initialize cache
cache_responses = {}

# Initialize Africa's Talking
username = os.environ.get('AFRICAS_TALKING_USERNAME')
api_key = os.environ.get('AFRICAS_TALKING_API_KEY')

africastalking.initialize(username, api_key)


def print_env():
    print(f'username: {username}')
    print(f'api_key: {api_key}')


class SendSMS():
    sms = africastalking.SMS

    def sending(self):
        # Set the numbers in international format
        recipients = ["+255789723254"]

        # Set your message
        message = "Hello, Africa's Talking!"

        # Set your shortCode or senderId
        sender = "NEPALS"

        try:
            response = self.sms.send(message, recipients, sender)
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
