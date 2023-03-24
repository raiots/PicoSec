
from dotenv import load_dotenv
import os

from app import scheduler
from adapter.weather import WeatherAlert
from adapter.notifiy import Notifier

load_dotenv()
noty = Notifier(wechat_send_key=os.getenv('SEVER_CHAN_KEY'))

@scheduler.task('cron', id='wind_alert', hour='09', minute='47')
def wind_alert():
    # weather = WeatherAlert('51.5074', '0.1278', 'b7a4d4a0f7c4e4d4b4a4d4a0f7c4e4d4')
    load_dotenv()
    weather = WeatherAlert("40.6879", "122.1223", os.getenv('API_KEY'))
    if weather.daily_wind_alert():
        send_str = ''
        for k, v in weather.daily_wind_alert().items():
            send_str += k + ': ' + str(v) + 'km/h\n'
        noty.send_wechat_msg(send_str)
