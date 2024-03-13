# Weather Forecast 5 Days

## CS50P Final Project (edX: henrywat_8)
## by Henry Wat (henrywat@gmail.com)
## 12 March 2024

#### Video Demo: [https://www.youtube.com/watch?v=weX9Vc48Mvo](https://www.youtube.com/watch?v=weX9Vc48Mvo)
#### Github : [https://github.com/henrywat/HarvadX-CS50P/tree/main/project](https://github.com/henrywat/HarvadX-CS50P/tree/main/project)
#### Description: The objectives of this project is calling OpenWeatherMap API to provide weather forecast with in 5 days to user.

Here is a sample output of the program.

```
Welcome to the Weather Forecast 5 Days! (provided by OpenWeatherMap)

Enter a city name : Vancouver
Enter forecast date (YYYY-MM-DD): 2024-2-30
Invalid date format or date. Please enter a date in YYYY-MM-DD format.
Enter forecast date (YYYY-MM-DD): 2024-3-1
Fetching weather forecast for Vancouver on 2024-3-1...
Actual weather for Vancouver: Forecast data for the specific date not found.
Try again? (y/n): y

Enter a city name : Calgary
Enter forecast date (YYYY-MM-DD): 2024-3-12
Fetching weather forecast for Calgary on 2024-3-12...
Actual weather for Calgary: Weather: Clouds, broken clouds, Temp: 7.13°C
Try again? (y/n): y

Enter a city name : Nagoya
Enter forecast date (YYYY-MM-DD): 2024-03-15
Fetching weather forecast for Nagoya on 2024-03-15...
Actual weather for Nagoya: Weather: Clear, clear sky, Temp: 16.87°C
Try again? (y/n): n
```

1. To run this python program, install the following three packages in your environment.
- request, send API request to OpenWeatherMap server.
- request_mock, provides a building block to stub out the HTTP requests portions of the testing code.
- pytest, a efficient, small and readable test package.
*you might install packages via requirements.txt*

2. Open the project.py and update the API key of your own.
- API_KEY = '{your_API_key}'

3. execute the project.py file.

---

### Program explanation:

**main()** - get user input of country and date via CLI, pass to 'validate_date' function for date format checking, then call the '*fetch_weather_data*' and display corresponding data.

**validate_date(String date_str)** - return True if the date_str in the format 'YYYY-MM-DD' only.

**fetch_weather_data(String location, String the_date)** - send requests to OpenWeatherMap API and pass the desired data to '*format_weather_data*' for output formatting.

**format_weather_data(String weather_data)** - extract data from json string and return formatted output to '*main()*'