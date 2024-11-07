# weather_service.py
import requests
from config import API_KEY, BASE_URL  # Changed to absolute imports

def get_weather(city, unit='metric'):
    """Fetches weather data for a given city."""
    try:
        url = f"{BASE_URL}?q={city}&units={unit}&appid={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the data as a dictionary
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return {}
