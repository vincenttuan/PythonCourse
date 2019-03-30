a = 100
b = 0
try:
    c = a / b
except ZeroDivisionError as e:
    print('b不可=0')
    print(e)
else:
    print(c)
