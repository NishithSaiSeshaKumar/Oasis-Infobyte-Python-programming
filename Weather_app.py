import requests
import json

# Replace with your own OpenWeatherMap API key
API_KEY = 'ddaf6c9efcc3caa799c66dbba3126b46'

def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # You can change units (e.g., 'imperial' for Fahrenheit)
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_conditions = data["weather"][0]["description"]

            print(f"Weather in {city_name}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Conditions: {weather_conditions}")
        else:
            print(f"Could not fetch weather data for {city_name}.")
    except requests.exceptions.RequestException:
        print("Failed to connect to the weather API.")

if __name__ == "__main__":
    print("Command-line Weather App")

    while True:
        city_name = input("Enter a city name: ").strip()
        if not city_name:
            print("City name cannot be empty. Please try again.")
        else:
            get_weather(city_name)
            break
