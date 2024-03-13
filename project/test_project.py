from project import *
import requests_mock

# below is the API key of openweatherrmap and the API URL
FORECAST_API_URL = "http://api.openweathermap.org/data/2.5/forecast"

def test_validate_date():
    assert validate_date("2023-01-01") == True
    assert validate_date("01-01-2023") == False
    assert validate_date("2023-02-30") == False
    assert validate_date("2024-02-29") == True
    assert validate_date("2023-02-29") == False
    assert validate_date("2050-12-31") == True
    assert validate_date("2000-01-01") == True
    assert validate_date("2023-04-30") == True
    assert validate_date("2023-04-31") == False
    assert validate_date(" 2023-01-01 ") == False

def test_format_weather_data():
    data = {"weather": [{"main": "Clear", "description": "clear sky"}], "main": {"temp": 25}}
    assert format_weather_data(data) == "Weather: Clear, clear sky, Temp: 25°C"

    data = {"weather": [{"main": "Clear", "description": "clear sky"}], "main": {"temp": 25}}
    expected = "Weather: Clear, clear sky, Temp: 25°C"
    assert format_weather_data(data) == expected

    data = {"weather": [{"main": "Rain", "description": "light rain"}], "main": {"temp": 16}}
    expected = "Weather: Rain, light rain, Temp: 16°C"
    assert format_weather_data(data) == expected

    data = {"main": {"temp": 20}}
    expected = "Error formatting weather data."
    assert format_weather_data(data) == expected

    data = {"weather": [{"main": "Clouds", "description": "overcast clouds"}]}
    expected = "Error formatting weather data."
    assert format_weather_data(data) == expected

    data = {}
    expected = "Error formatting weather data."
    assert format_weather_data(data) == expected

def test_fetch_weather_data_success():
    with requests_mock.Mocker() as m:
        m.get(FORECAST_API_URL, json={
            "list": [
                {"dt": 1710277200, "weather": [{"main": "Clouds", "description": "overcast clouds"}], "main": {"temp": 10}}
            ]
        })
        # Assuming the timestamp 1600000000 corresponds to the date input below
        expected_output = "Weather: Clouds, overcast clouds, Temp: 10°C"
        assert fetch_weather_data("ABCCity", "2024-03-12") == expected_output

def test_fetch_weather_data_not_found():
    with requests_mock.Mocker() as m:
        m.get(FORECAST_API_URL, json={"list": []})
        expected_output = "Forecast data for the specific date not found."
        assert fetch_weather_data("ABCCity", "2023-01-01") == expected_output

def test_fetch_weather_data_api_failure():
    with requests_mock.Mocker() as m:
        m.get(FORECAST_API_URL, status_code=500)
        expected_output = "Failed to fetch weather data."
        assert fetch_weather_data("ABCCity", "2023-01-01") == expected_output