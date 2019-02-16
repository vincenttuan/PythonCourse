import json
import requests

url = 'https://data.tycg.gov.tw/api/v1/rest/datastore/a1b4714b-3b75-4ff8-a8f2-cc377e4eaa0f?format=json&limit=300'
youbike = requests.get(url).text
youbike = json.loads(youbike)
#print(youbike)

for item in youbike['result']['records']:
    bemp = int(item['bemp'])
    sbi = int(item['sbi'])
    if bemp>=20 and sbi >= 20:
        print(item)