# weather_app/utils.py

from datetime import datetime

def parse_weather_data(data, unit):
    """Parses weather data JSON response and returns formatted weather information."""
    try:
        city_name = data["name"]
        main = data["main"]
        weather = data["weather"][0]
        wind = data["wind"]
        
        # Extract key data points
        temperature = main["temp"]
        feels_like = main["feels_like"]
        humidity = main["humidity"]
        weather_description = weather["description"].capitalize()
        wind_speed = wind["speed"]
        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S")
        sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S")

        # Generate weather ASCII art
        ascii_art = get_ascii_art(weather_description)

        # Unit for temperature
        temp_unit = "°C" if unit == "metric" else "°F" if unit == "imperial" else "K"

        return (
            f"{ascii_art}\n"
            f"City: {city_name}\n"
            f"Temperature: {temperature}{temp_unit} (Feels like {feels_like}{temp_unit})\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s\n"
            f"Description: {weather_description}\n"
            f"Sunrise: {sunrise}\n"
            f"Sunset: {sunset}"
        )
    except (KeyError, TypeError):
        return "Error: Unexpected data format in the response."

def get_ascii_art(description):
    """Returns ASCII art based on the weather description."""
    if "clear" in description.lower():
        return "☀️ Clear Skies ☀️"
    elif "cloud" in description.lower():
        return "☁️ Cloudy ☁️"
    elif "rain" in description.lower():
        return "🌧️ Rainy 🌧️"
    elif "snow" in description.lower():
        return "❄️ Snowy ❄️"
    elif "storm" in description.lower():
        return "⛈️ Stormy ⛈️"
    else:
        return "🌤️ Mixed Weather 🌤️"
