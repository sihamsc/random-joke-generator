import requests

def get_weather(city):
    """Fetch weather data for a given city"""
    api_key = "your_openweather_api_key"  # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        return f"Current temperature in {city} is {temp}°C with {weather}."
    else:
        return "Failed to fetch weather data. Check the city name or API key."

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_info = get_weather(city)
    print(weather_info)
