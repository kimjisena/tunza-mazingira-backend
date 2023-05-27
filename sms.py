import africastalking
import os

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
            # sample response
            # {
            #     SMSMessageData: {
            #     Message: 'Sent to 1/1 Total Cost: TZS 22.0000',
            #     Recipients: [ [Object] ] 
            #     }
            # }
        except Exception as e:
            print(f'Tenemos una problema: {e}')