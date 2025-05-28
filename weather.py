import requests
import os

def get_weather(city):
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    if not api_key:
        raise ValueError("API key not found in environment variables")
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description']}, {data['main']['temp']}°C")
    else:
        print(f"Error fetching weather: {response.status_code}")

# Example usage
get_weather("Toronto")
