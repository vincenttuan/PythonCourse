import requests
from bs4 import BeautifulSoup

def append_list_pm25():
    url = 'https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=1'
    html = requests.get(url)
    sp = BeautifulSoup(html.text, 'html.parser')
    rs = sp.find_all("tr", {"align": "center", "style": "border-width:1px;border-style:Solid;"})
    for r in rs:
        name = r.find('a')
        pm25 = r.find_all('span')
        dic = {}
        dic.setdefault('name',   name.text.strip())
        dic.setdefault('pm25',   pm25[0].text.strip())
        dic.setdefault('pm25_1', pm25[1].text.strip())
        list.append(dic)

list = []
append_list_pm25()
print(list)

name = input('請輸入地區 ? (例如:林口, 桃園) : ')
print(name)




