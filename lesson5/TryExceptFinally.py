a = 100
b = [5, 10, 0]
try:
    c = a / b[3]
except ZeroDivisionError:
    print('b不可=0')
else:
    print(c)
finally:
    print('程式結束')
