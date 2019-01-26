'''
Celsius 攝氏 = (華氏-32)*5/9
Fah 華氏 = 攝氏*(9/5)+32
'''

c = float(input('請輸入攝氏 : '))
f = c*(9/5)+32
print("攝氏:%.2f = 華式:%.2f" % (c, f))

f = float(input('請輸入華氏 : '))
c = (f-32)*5/9
print("華式:.2%f = 攝氏:%.2f" % (f, c))


