from flask import Flask
from flask_apscheduler import APScheduler
import schedule

app = Flask(__name__)


# initialize scheduler
scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
# scheduler.api_enabled = True
scheduler.init_app(app)
scheduler.start()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'



class Config(object):
    SCHEDULER_API_ENABLED = True
    
app.config.from_object(Config())

if __name__ == '__main__':
    app.run()
