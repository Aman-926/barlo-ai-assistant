import requests


def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,apparent_temperature,weather_code",
        "temperature_unit": "fahrenheit",
    }

    response = requests.get(url, params=parameters, timeout=10)
    response.raise_for_status()

    data = response.json()

    return data["current"]