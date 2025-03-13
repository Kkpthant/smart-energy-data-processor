import requests

#API Endpoint for solar & wind energy data
API_URL = "https://api.open-meteo.com/v1/forecast"

#Parameters: Latitude, Longitude, Energy data fields
params = {
    "latitude": 51.509865, # London example
    "longitude": -0.118092,
    "current": "temperature_2m,wind_speed_10m"
}

#Fetch data from API
response = requests.get(API_URL, params=params)

#Convert to JSON
if response.status_code == 200:
    energy_data = response.json()
    print("Energy data:", energy_data)
else:
    print("Error fetching data:", response.status_code)