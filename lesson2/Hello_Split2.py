str1 = '60.0,170.0'
w, h = str1.split(',')
print(w)
print(h)

str2 = 'w=70.0,h=180.0'
w, h = str2.replace('w=','').replace('h=','').split(',')
print(w)
print(h)

str3 = 'w=80.0,h=190.0'
w, h = (item.split('=')[1] for item in str3.split(','))
print(w)
print(h)

