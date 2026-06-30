import os
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    base_url = "http://api.weatherapi.com/v1/current.json"
    city = "Paris"
    response = requests.get(base_url, params={"key": api_key, "q": city})
    data = response.json()
    temp = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]
    print(f"Weather in {city}: {temp}°C, {condition}")


if __name__ == "__main__":
    get_weather()
