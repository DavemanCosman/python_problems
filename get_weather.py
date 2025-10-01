import requests

def get_weather(api_key, city):
    base_url = "http://api.weatherapi.com/v1/forecast.json" # https://www.weatherapi.com/my/
    params = {
        "key": api_key,
        "q": city,
        "days": 1  # Fetch forecast for today
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

api_key = "605872dc53874f238ed155913252309" # obviously this would be secured in prod envs
city = "London"
weather_data = get_weather(api_key, city)
print(weather_data)

