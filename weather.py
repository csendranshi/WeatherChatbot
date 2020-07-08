import requests
def Weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    API_key = "a4d16d4e77a95d6061d1be0295844ee8"

    Final_url = base_url + "appid=" + API_key + "&q=" + city + "&units=metric"
    weather_data = requests.get(Final_url).json()

    return weather_data['main']