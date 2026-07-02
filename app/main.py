import os
import requests


def get_weather() -> None:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        print("API_KEY is missing")
        return

    base_url = "http://api.weatherapi.com/v1/current.json"
    city = "Paris"

    response = requests.get(base_url, params={"key": api_key, "q": city})
    if response.status_code != 200:
        print(f"Error: {response.status_code}")
        return

    data = response.json()
    current_data = data.get("current", {})
    temp = current_data.get("temp_c")
    condition = current_data.get("condition", {}).get("text")
    print(f"Weather in {city}: {temp}°C, {condition}")


if __name__ == "__main__":
    get_weather()
