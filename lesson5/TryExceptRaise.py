a = 100
b = 0
try:
    if b == 0:
        raise Exception('b不可=0')
    c = a / b
except Exception as e:
    print(e)
else:
    print(c)
