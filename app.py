from flask import Flask
from sms import SendSMS, print_env

app = Flask(__name__)

@app.route("/")
def hello_world():
    # print env variables
    print_env()

    # send sms
    SendSMS().sending()
    return {
        "message": "Hello World",
        "success": True,
    }
