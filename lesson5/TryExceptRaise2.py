def calc(a, b):
    if b == 0:
        raise Exception('b不可=0')
    c = a / b
    print(c)

try:
    calc(100, 0)
except Exception as e:
    print(e)
