import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
url = 'https://tw.sports.yahoo.com/nba/standings/'
html = requests.get(url, headers=headers)
sp = BeautifulSoup(html.text, 'html.parser')

#<span data-tst="first-name" class="" data-reactid="40">布魯克林</span>
#<div class="Fw(n) Fz(12px)" data-reactid="44">籃網</div>
#<span class="" data-reactid="46">20</span>
print(sp.find("span", {"data-reactid":"40"}).text.strip(), end="");
print(sp.find("div", {"data-reactid":"44"}).text.strip(), end=" ");
print(sp.find("span", {"data-reactid":"46"}).text.strip());

#<span data-tst="first-name" class="" data-reactid="53">洛杉磯</span>
#<div class="Fw(n) Fz(12px)" data-reactid="57">湖人</div>
#<span class="" data-reactid="59">31</span>
print(sp.find("span", {"data-reactid":"53"}).text.strip(), end="");
print(sp.find("div", {"data-reactid":"57"}).text.strip(), end=" ");
print(sp.find("span", {"data-reactid":"59"}).text.strip());



