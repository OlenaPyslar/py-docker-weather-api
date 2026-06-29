import os
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    BASE_URL = "http://api.weatherapi.com/v1/current.json"
    CITY = "Paris"
    response = requests.get(BASE_URL, params={"key": api_key, "q": CITY})
    data = response.json()
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(f"Weather in {CITY}: {temp}°C, {condition}")


if __name__ == "__main__":
    get_weather()
