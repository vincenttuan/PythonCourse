
s = 'she sell sea shell on the sea shore'
print(s.find('sea'))
print(s.find('happy'))

keyword = 'sea'
if s.find(keyword) != -1 :
    print(s + " 內容中有 " + keyword)
else :
    print(s + " 內容中沒有 " + keyword)
