from flask import Flask
from flask_apscheduler import APScheduler

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': 'app:job1',
            'args': (1, 2),
            'trigger': 'interval',
            'seconds': 5
        }
    ]

    SCHEDULER_API_ENABLED = True


if __name__ == '__main__':
    app.config.from_object(Config())
    app.run()
