import requests
from datetime import datetime

# below is the FREE API key of openweatherrmap and the API URL
API_KEY = '{your_API_key}'
FORECAST_API_URL = "http://api.openweathermap.org/data/2.5/forecast"

def main():
    print("\nWelcome to the Weather Forecast 5 Days! (provided by OpenWeatherMap)")
    while True:
        # ask for the location
        location = input("\nEnter a city name : ").strip()

        # ask for the valid date
        date = ""

        while True:
            date = input("Enter forecast date (YYYY-MM-DD): ").strip()
            if not validate_date(date):
                print("Invalid date format or date. Please enter a date in YYYY-MM-DD format.")
            else:
                print(f"Fetching weather forecast for {location} on {date}...")
                break
        
        # fetch data from openweathermap
        weather_data = fetch_weather_data(location, date)
        print(f"Actual weather for {location}: {weather_data}")
        
        if input("Try again? (y/n): ").lower() != 'y':
            break

''' date format validation (YYYY-MM-DD) '''
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

''' fetech weather data from openweather API '''
def fetch_weather_data(location, the_date):
    try:
        # convert the date to a datetime object
        target_date = datetime.strptime(the_date, "%Y-%m-%d")
        
        # call the API
        response = requests.get(FORECAST_API_URL, params={'q': location, 'appid': API_KEY, 'units': 'metric', 'mode': 'json'})
        response.raise_for_status()
        forecast_data = response.json()

        # find the weather of the target date
        for forecast in forecast_data['list']:
            forecast_time = datetime.fromtimestamp(forecast['dt'])
            if forecast_time.date() == target_date.date():
                return format_weather_data(forecast)
        
        return "Forecast data for the specific date not found."
    except requests.RequestException:
        return "Failed to fetch weather data."


''' convert the API weather date to friendly format '''
def format_weather_data(weather_data):
    try:
        main_weather = weather_data['weather'][0]['main']
        description = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        return f"Weather: {main_weather}, {description}, Temp: {temperature}°C"
    except KeyError:
        return "Error formatting weather data."
    
if __name__ == "__main__":
    main()