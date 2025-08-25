import http.client
import json

def get_weather(city):
    api_key = "OpenWeather Api"  # Replace with OpenWeather API key
    conn = http.client.HTTPSConnection("api.openweathermap.org")
    url = f"/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    conn.request("GET", url)
    response = conn.getresponse()

    if response.status == 200:
        data = json.loads(response.read())
        print(f"Weather in {city}:\n")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"☁ Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
    else:
        print("City not found or error fetching data.")
city = input("Enter city name: ")
get_weather(city)
