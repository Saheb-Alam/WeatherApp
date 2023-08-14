import requests
import json

city= input("enter the city's name whose weather details you want?\n")

url =f"https://api.weatherapi.com/v1/current.json?key=0b2bbb225a1f45af81595847231208&q={city}"

r= request.get(url)
print(r.text)
weather = json.loads(r.text)
print(weather["current"]["temp_c"])