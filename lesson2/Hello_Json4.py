import json
import requests

url = 'https://samples.openweathermap.org/data/2.5/find?q=London&appid=b6907d289e10d714a6e88b30761fae22'
weather = requests.get(url).text
weather = json.loads(weather)
print(weather)

temp = weather['list'][0]['main']['temp'] # string
print(temp)

temp = float(temp) - 273.15 # float
print(temp)

icon = weather['list'][0]['weather'][1]['icon']
print(icon)

url = 'http://openweathermap.org/img/w/' + icon + '.png'
icon_data = requests.get(url).content
#file = open('weather.png', 'wb')
#file.write(icon_data)

with open('weather.png', 'wb') as file:
    file.write(icon_data)
