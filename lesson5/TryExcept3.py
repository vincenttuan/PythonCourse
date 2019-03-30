a = 100
b = [5, 10, 0]
try:
    c = a / b[3]
except ZeroDivisionError as e:
    print('b不可=0')
    print(e)
except IndexError as e:
    print('index 超過 ' + str(len(b)-1))
    print(e)

else:
    print(c)
