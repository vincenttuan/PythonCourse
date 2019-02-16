import random

x = {'apple', 'banana'}
print(type(x))
print(x)
x.add('apple')
print(x)
print(len(x))
print("-------------------")

lotto = set()
print(type(lotto))

while len(lotto) < 6 :
    lotto.add(random.randint(1, 46))

print(lotto)