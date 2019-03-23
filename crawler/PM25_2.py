import requests
from bs4 import BeautifulSoup

url = 'https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=1'
html = requests.get(url)

#print(html.text)

sp = BeautifulSoup(html.text, 'html.parser')
#print(len(sp.select("title")));
#print(sp.select("title")[0]);
#print(sp.select("title")[0].text);
print(sp.select("title")[0].text.strip());

print(sp.find("span", {"id":"ctl08_labText1"}).text.strip());

