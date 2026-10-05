from weather import get_weather, get_weather_description


print("Barlo is online.")

weather = get_weather(43.10, -75.23)


temperature = weather ["temperature_2m"]
feels_like = weather["apparent_temperature"]
condition = get_weather_description(weather["weather_code"])

print(
    f"Barlo: It's currently {temperature}°F and {condition}. "
    f"It feels like {feels_like}°F outside."
)
