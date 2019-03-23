import requests
from bs4 import BeautifulSoup

class PM25:
    name = ''
    pm25 = ''
    pm25_1 = ''

    def __str__(self) -> str:
        return self.name + "," + self.pm25 + "," + self.pm25_1


def append_pm25_list():
    url = 'https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=1'
    html = requests.get(url)
    sp = BeautifulSoup(html.text, 'html.parser')
    rs = sp.find_all("tr", {"align": "center", "style": "border-width:1px;border-style:Solid;"})
    for r in rs:
        name = r.find('a')
        value = r.find_all('span')

        pm25 = PM25()
        pm25.name = name.text.strip()
        pm25.pm25 = value[0].text.strip()
        pm25.pm25_1 = value[1].text.strip()

        pm25_list.append(pm25)


def get_pm25(name):
    for pm25 in pm25_list:
        if pm25.name == name:
            return pm25


pm25_list = []
append_pm25_list()
print(list)

pm25 = get_pm25('林口')
print(pm25)
print(pm25.name)
print(pm25.pm25)
print(pm25.pm25_1)


