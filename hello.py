import requests
import json

# --- Configuration ---
LATITUDE = 48.37  # Latitude for Augsburg
LONGITUDE = 10.90  # Longitude for Augsburg
API_ENDPOINT = "https://api.open-meteo.com/v1/forecast"

# Parameters for the API request
params = {
    "latitude": LATITUDE,
    "longitude": LONGITUDE,
    "hourly": "temperature_2m,weathercode",  # Specify the data you want
    "current_weather": True,  # Include current weather data
    "timezone": "auto"  # Automatically adjust timezone
}

# Make the API request
response = requests.get(API_ENDPOINT, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()
    print(weather_data.keys())  # Print the keys of the JSON response
    data=json.dumps(weather_data, indent=4)
    print(type(data))
    print(data)  # Pretty-print the JSON data
else:
    print(f"Error: Unable to fetch weather data (Status code: {response.status_code})")