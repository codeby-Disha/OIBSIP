import requests
import os
from dotenv import load_dotenv
load_dotenv()

def get_weather(city):
    # Step 1: Convert city name to latitude & longitude
    geo_url = os.getenv("GEO_URL")
    geo_params = {
        "name": city,
        "count": 1
    }

    geo_response = requests.get(geo_url, params=geo_params)
    geo_data = geo_response.json()

    if "results" not in geo_data:
        print("❌ City not found!")
        return

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

    # Step 2: Fetch current weather data
    weather_url = os.getenv("WEATHER_URL")
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
        "hourly": "relativehumidity_2m"
    }

    weather_response = requests.get(weather_url, params=weather_params)
    weather_data = weather_response.json()

    # Step 3: Extract required details
    temperature = weather_data["current_weather"]["temperature"]
    wind_speed = weather_data["current_weather"]["windspeed"]
    weather_code = weather_data["current_weather"]["weathercode"]

    humidity = weather_data["hourly"]["relativehumidity_2m"][0]

    # Step 4: Simple weather condition mapping
    weather_conditions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        61: "Rain",
        71: "Snow",
        95: "Thunderstorm"
    }

    condition = weather_conditions.get(weather_code, "Unknown")

    # Step 5: Display output
    print("\n🌤 Current Weather Report")
    print("----------------------------")
    print(f"📍 City: {city}")
    print(f"🌡 Temperature: {temperature}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"☁ Condition: {condition}")
    print(f"💨 Wind Speed: {wind_speed} km/h")


# ---- Main Program ----
if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
