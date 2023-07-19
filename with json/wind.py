import requests

import json

f = open("./z.json", "r")

# API_url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_wind():
    date_input = input("Enter the date (YYYY-MM-DD): ")
    # response = requests.get(API_url)
    # if response.status_code == 200:
    response = json.load(f)

    weather_data = response
    for data in weather_data["list"]:
        if data["dt_txt"].startswith(date_input):
            print(f"Wind Speed on {date_input}: {data['wind']['speed']}")
            return
    print("No wind speed data found for the given date.")
    return 
    # else:
    #     print("Failed to retrieve wind speed data.")