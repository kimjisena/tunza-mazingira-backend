from flask import Flask
from sms import SendSMS, print_env, cache_responses
from flask_apscheduler import APScheduler

# set configuration values


class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config.from_object(Config())

# initialize scheduler
scheduler = APScheduler()
scheduler.init_app(app)

@scheduler.task('interval', id='send_sms', seconds=30)
def send_sms():
    # Code to send SMS goes here
    print("Sending SMS...")
    # print env variables
    # print_env()
    # send sms
    SendSMS().sending()


# @scheduler.scheduled_job('cron', id='send_weekly_sms', week='*', day_of_week='sun')
# def send_weekly_reminder():
#     print('This a weekly reminder to get rid of your trash...')

# start the main scheduler
# scheduler.start()


@app.route("/")
def index():
    return {
        "message": "Index route",
        "success": True,
    }


@app.route("/informations")
def infos():
    return cache_responses


scheduler.start()