a = 100
b = [5, 10, 0]
try:
    c = a / b[1]
except (ZeroDivisionError, IndexError) as e:
    print(e)
else:
    print(c)
