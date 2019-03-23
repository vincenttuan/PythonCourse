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

print(sp.find("a", {"href":"HourlyData.aspx"}).get('title').strip());

rs = sp.find_all("tr", {"align":"center", "style":"border-width:1px;border-style:Solid;"})

for r in rs:
    #print(r.text.strip())
    name = r.find('a').text.strip()
    pm25 = r.find_all('span')

    #print("%s %s %s" % (name, pm25[0].text.strip(), pm25[1].text.strip()))

    print(name, end=" ")
    for p in pm25:
        print(p.text.strip(), end=" ")
    print()


