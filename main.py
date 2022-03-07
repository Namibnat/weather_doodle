"""Just get weather data and doodle"""

import datetime
import json
import os
import requests


def get_weather():
    locations = {
        "Birmingham": "12723",
        "London": "44418"
    }
    for name, location in locations.items():
        date = datetime.datetime.now().strftime("%Y/%m/%d")
        url = f"https://www.metaweather.com/api/location/{location}/{date}/"
        response = requests.get(url)
        data = response.json()
        print(f"{name}: Air Pressure: {data[0]['air_pressure']}, Temperature: {data[0]['the_temp']}")

if __name__ == "__main__":
    get_weather()