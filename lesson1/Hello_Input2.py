import math

r = float(input('請輸入半徑(cm) r = '))
area = r*r*3.14
print(area)
area = r*r*math.pi
print(area)
area = r**2*math.pi
print(area)
area = math.pow(r, 2) * math.pi
print(area)

print('%.2f' % area)
print('圓面積是 : %.2f cm^2' % area)
