str = 'w=60.0,h=170.0'
print(str)
print('----------------')
s1 = str.split(',')
print(s1) # 陣列
print(s1[0])
print(s1[1])
print('----------------')
w = s1[0].split('=')
print(w) # 陣列
w = w[1]
print(w)
print('----------------')
w = str.split(",")[0].split("=")[1]
h = str.split(",")[1].split("=")[1]
w = float(w)
h = float(h)
bmi = w / pow(h/100, 2)
print(bmi)
print("%.2f" % bmi)