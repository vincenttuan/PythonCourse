def hi():
    print("Hello Python")

def calc(x, y):
    return x + y

def calc2(x=3, y=5):
    return x + y

def calc3(*score):
    return sum(score)
    #return sum(score, 1) # 計算完結果之後 +1

def bmi(h, w):
    return w/pow(h/100, 2)


hi()

calc = calc(10, 20)
print(calc)

bmi = bmi(170, 60)
print("%.2f" % bmi)

print(calc2())
print(calc2(10))
print(calc2(y=10))
print(calc2(10, 20))

print(calc3(100, 90, 80, 70))