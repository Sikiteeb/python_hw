# Sigrid Hanni
import requests
import datetime


# Kelvin, Fahrenheit -> Celsius conversion is easy by adding units=metric, to the request_url
# PyCharm complained about the long string
def get_weather_forecast():
    request_url = "http://api.openweathermap.org/data/2.5/weather?appid=b4dce5a35473f40d8a73bdcebeeb9281&lat=59.40" \
                  "&lon=24.69&units=metric"

    response = requests.get(request_url)

    data = response.json()
    city = data["name"]
    weather_description = data["weather"][0]["description"]
    feels_like = data["main"]["feels_like"]
    pressure = data["main"]["pressure"]
    avg_temperature = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]
    min_temperature = data["main"]["temp_min"]
    max_temperature = data["main"]["temp_max"]

    today = datetime.date.today()

    print("-----------------")
    print("Weather forecast")
    print("-----------------")
    # I chose to do Estonian version of date, code for the date in example would be:
    # print("Today is " + today.strftime("%Y-%m-%d"))

    print("Today is " + today.strftime("%d.%m.%Y"))
    print("City: " + city)
    print("Weather description: " + weather_description)
    print("Feels like: " + str(feels_like))
    print("Pressure: " + str(pressure))
    print("Temperature (in Celsius): " + str(avg_temperature))
    print("Wind: " + str(wind_speed) + " m/s")
    print("Minimum temperature: " + str(min_temperature))
    print("Maximum temperature: " + str(max_temperature))


# Pycharm recommended this
if __name__ != '__main__':
    pass
else:
    get_weather_forecast()
