import requests
import json
import win32com.client as wincom

# Get the city name from user input
city = input("Enter name of the city\n")

# Define the API key and the URL
api_key = "!!!YOUR API!!!" #-> PLEASE VISIT FOR FREE API https://www.weatherapi.com/
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

# Make a request to the weather API
response = requests.get(url)
data = response.json()

# Extract the current temperature
temperature = data["current"]["temp_c"]

# Use win32com client to convert text to speech
speaker = wincom.Dispatch("SAPI.SpVoice")
speaker.Speak(f"Ankit the current temperature in {city} is {temperature} degrees Celsius.")
