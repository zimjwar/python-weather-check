# Main.py
import json
import sys
import os

# Adding the path of the project to sys.path so modules can be imported
sys.path.append("C:/Users/Zinhle/Desktop/python-weather-check")

# Importing necessary modules
from weather_service import get_weather  # To get weather data
from history import add_to_history, show_history, clear_history  # For managing search history
from config import API_KEY, BASE_URL, DEFAULT_CITY, DEFAULT_UNIT  # For API settings and default values

# Function to format the weather information from the API response
def format_weather_info(weather_info):
    """Formats the weather information from the API response."""
    try:
        temp = weather_info['main']['temp']
        description = weather_info['weather'][0]['description']
        humidity = weather_info['main']['humidity']
        return f"Temperature: {temp}°\nDescription: {description}\nHumidity: {humidity}%"
    except KeyError as e:
        return f"Error: Missing key {e} in the weather data. Please check the API response."

# Main function to run the app
def main():
    print("Welcome to the Enhanced Weather App!")

    # Main loop for user interaction
    while True:
        print("\nOptions:")
        print("1. Check Weather")
        print("2. View Search History")
        print("3. Clear Search History")
        print("4. Exit")
        
        # Get the user's choice
        choice = input("\nEnter choice (1/2/3/4): ").strip()

        if choice == "1":
            # Option to check the weather
            city = input("Enter city name (or press Enter for default): ").strip() or DEFAULT_CITY
            unit = input("Choose unit - (M)etric, (I)mperial, (S)tandard (or press Enter for default): ").strip().lower()
            
            # Set unit based on user input
            unit = "metric" if unit == "m" else "imperial" if unit == "i" else "standard" if unit == "s" else DEFAULT_UNIT

            # Fetch weather information using the get_weather function
            weather_info = get_weather(city, unit)

            # Print the weather information in a readable format
            formatted_weather_info = format_weather_info(weather_info)
            print("\n" + formatted_weather_info)

            # Optional: Print the raw weather info (formatted as JSON for clarity)
            print("\nRaw weather data (JSON format):")
            print(json.dumps(weather_info, indent=2))

            # Log the search to the history
            add_to_history(f"{city} ({unit}): {formatted_weather_info}")

        elif choice == "2":
            # Option to show search history
            show_history()

        elif choice == "3":
            # Option to clear search history
            clear_history()

        elif choice == "4":
            # Option to exit the app
            print("Goodbye!")
            break

        else:
            # Invalid choice handling
            print("Invalid option. Please try again.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
