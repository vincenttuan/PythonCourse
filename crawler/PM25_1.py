from urllib.parse import urlparse

url = 'https://taqm.epa.gov.tw/pm25/tw/PM25A.aspx?area=1'
pr = urlparse(url)  # 利用 urllib 套件的 urlparse 函式可以解析網址
print(pr)  # pr -> ParseResult

print("scheme={}".format(pr.scheme))
print("netloc={}".format(pr.netloc))
print("port={}".format(pr.port))
print("path={}".format(pr.path))
print("query={}".format(pr.query))
