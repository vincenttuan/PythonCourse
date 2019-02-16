import json

file = open('weather.json', 'r')
weather = file.read()
weather = json.loads(weather)

print(weather['main']['temp'])