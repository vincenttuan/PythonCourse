# -*- coding:UTF-8 -*-
import math

h = 170.0
w = 60.0
bmi = w / ((h/100)**2)
print('身體評量指數 bmi = %.2f' % bmi)
bmi = w / math.pow(h/100, 2)
print('bmi = %.2f' % bmi)
print('h = %.2f, w = %.2f, bmi = %.2f' % (h, w, bmi))
print("h = {0}, w = {1}, bmi = {2}".format(h, w, bmi))

if (bmi >= 18.0 and bmi < 23) :
    print('正常')
else :
    print('不正常')

if 18 <= bmi < 23:
    print('正常')
else:
    print('不正常')

