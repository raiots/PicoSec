import os
import requests
import json
from dotenv import load_dotenv


class WeatherAdapter:
    def __init__(self, lat, lon, api_key):
        self.location = (lat, lon)
        self.api_key = api_key

    def get_weather(self):
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (
            self.location[0], self.location[1], self.api_key)
        response = requests.get(url)
        data = json.loads(response.text)
        print(data)
        # with open('weather.json', 'w') as f:
        #     json.dump(data, f)
        # f.close()


def get_wether():
    load_dotenv()
    weather = WeatherAdapter("40.6879", "122.1223", os.getenv('API_KEY'))
    weather.get_weather()


if __name__ == '__main__':
    get_wether()
