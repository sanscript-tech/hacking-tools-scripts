import requests
import json
import sys
from colorama import Fore, init
import config
# Autoreset on for Colorama
init(autoreset=True)
# Getting API Key from Config.py
api_key=config.api_key
# If the user doesn't enter the location
if len(sys.argv) != 2 :
	print("Enter location")
location = sys.argv[1]
# Calling the API
url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={api_key}"
response = requests.get(url)
data = json.loads(response.text)
print(Fore.CYAN + "Weather Details for the city " + data["name"])
print(Fore.BLUE + "Weather : " + data["weather"][0]["main"])
print(Fore.BLUE + "Temperature is " + str(data["main"]["temp"]) + "°C and it feels like " + str(data["main"]["feels_like"]) + "°C")
print(Fore.BLUE + "Wind Speed is " + str(data["wind"]["speed"]) + " m/sec")