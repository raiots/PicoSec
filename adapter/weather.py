import datetime
import os
import requests
import json
from dotenv import load_dotenv


def multiply_key_value(data, target_key, multiply_factor):
    """
    Multiply the value of a key in a dictionary by a factor
    :param data:
    :param target_key:
    :param multiply_factor:
    :return:
    """
    for key, value in data.items():
        if key == target_key:
            if isinstance(value, list):
                data[key] = [v * multiply_factor for v in value]
            else:
                data[key] = value * multiply_factor
        elif isinstance(value, dict):
            multiply_key_value(value, target_key, multiply_factor)
        elif isinstance(value, list):
            for i in range(len(value)):
                if isinstance(value[i], dict):
                    multiply_key_value(value[i], target_key, multiply_factor)
                else:
                    value[i] = value[i] * multiply_factor


class WeatherAdapter:
    def __init__(self, lat: str, lon: str, api_key: str):
        """
        :param lat: the latitude of the location
        :param lon: the longitude of the location
        :param api_key: api key for openweathermap
        """
        self.location = (lat, lon)
        self.api_key = api_key

        self.weather_data = self.get_weather()

    def get_weather(self):
        """
        Get the weather data from openweathermap
        :return:
        """
        url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=metric" % (
            self.location[0], self.location[1], self.api_key)
        response = requests.get(url)
        data = json.loads(response.text)

        multiply_key_value(data, 'wind_speed', 3.6)
        with open('weather.json', 'w') as f:
            json.dump(data, f)
        f.close()
        return data


class WeatherAlert(WeatherAdapter):
    def __init__(self, lat: str, lon: str, api_key: str):
        super().__init__(lat, lon, api_key)

    def daily_wind_alert(self):
        today_wind = {}
        for each_hour in self.weather_data["hourly"]:
            date_time_obj = datetime.datetime.fromtimestamp(each_hour["dt"])
            if date_time_obj.date() == datetime.date.today() and each_hour["wind_speed"] > 15:
                today_wind[date_time_obj.strftime("%H:%M")] = each_hour["wind_speed"]
        
        if today_wind:
            return today_wind
        else:
            return False


if __name__ == '__main__':
    load_dotenv()
    weather = WeatherAlert("40.6879", "122.1223", os.getenv('API_KEY'))
    print(weather.daily_wind_alert())
    