# # weather_app/history.py

# import os

# HISTORY_FILE = "weather_history.txt"

# def add_to_history(entry):
#     """Adds a weather search entry to the history file."""
#     with open(HISTORY_FILE, "a") as file:
#         file.write(entry + "\n")

# def show_history():
#     """Displays the search history from the history file."""
#     if os.path.exists(HISTORY_FILE):
#         with open(HISTORY_FILE, "r") as file:
#             print("\nWeather Search History:")
#             for line in file:
#                 print(line.strip())
#     else:
#         print("\nNo search history found.")

# def clear_history():
#     """Clears the search history file."""
#     if os.path.exists(HISTORY_FILE):
#         os.remove(HISTORY_FILE)
#         print("History cleared.")
#     else:
#         print("No history to clear.")

        # history.py
import os
import json

HISTORY_FILE = "search_history.json"

# Function to load the history from the file
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)
    return []

# Function to save the history to the file
def save_history(history):
    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=2)

# Function to add a search to the history
def add_to_history(search_entry):
    history = load_history()
    history.append(search_entry)
    save_history(history)

# Function to display the search history
def show_history():
    history = load_history()
    if history:
        print("\nSearch History:")
        for entry in history:
            print(entry)
    else:
        print("\nNo search history available.")

# Function to clear the search history
def clear_history():
    save_history([])  # Clear the history by saving an empty list
    print("\nSearch history cleared.")

