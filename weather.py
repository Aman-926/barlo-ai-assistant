import requests


def get_weather_description(code):
    weather_codes = {
        0: "clear",
        1: "mostly clear",
        2: "partly cloudy",
        3: "overcast",
        45: "foggy",
        48: "foggy",
        51: "light drizzle",
        53: "drizzle",
        55: "heavy drizzle",
        61: "light rain",
        63: "rain",
        65: "heavy rain",
        71: "light snow",
        73: "snow",
        75: "heavy snow",
        80: "light rain showers",
        81: "rain showers",
        82: "heavy rain showers",
        95: "thunderstorms",
    }

    return weather_codes.get(code, "unknown conditions")


def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    parameters = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,apparent_temperature,weather_code",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
        "temperature_unit": "fahrenheit",
        "timezone": "auto",
        "forecast_days": 1,
    }

    response = requests.get(url, params=parameters, timeout=10)
    response.raise_for_status()

    data = response.json()

    current = data["current"]
    daily = data["daily"]

    weather_data = {
        "temperature": current["temperature_2m"],
        "feels_like": current["apparent_temperature"],
        "weather_code": current["weather_code"],
        "high": daily["temperature_2m_max"][0],
        "low": daily["temperature_2m_min"][0],
        "precipitation_chance": daily["precipitation_probability_max"][0],
    }

    return weather_data