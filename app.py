from flask import Flask
from sms import SendSMS, print_env
from flask_apscheduler import APScheduler

# set configuration values
class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config.from_object(Config())

# initialize scheduler
scheduler = APScheduler()
scheduler.init_app(app)

@scheduler.task('interval', id='send_sms', seconds=2, misfire_grace_time=900)
def send_sms():
    # Code to send SMS goes here
    print("Sending SMS...")
    
    
    # print env variables
    print_env()
    return
    # send sms
    SendSMS().sending()

scheduler.start()

@app.route("/")
def index():
    return {
        "message": "Index route",
        "success": True,
    }
