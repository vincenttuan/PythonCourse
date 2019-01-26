import random

# 亂數取值
a = random.randint(1, 100)
b = random.randint(1, 100)
print(a)
print(b)
print(a);print(b)

x = 'python'
y = "3.7"

print(x + y)

c = a * 2 + b - b * 3
print(c)

c = a * 2\
    + b\
    - b * 3

print(c)

e = [1, 2, 3, 4];
print(e)
random.shuffle(e)  # 洗牌
print(e)

f = random.random()  # 0~1取值 float
print(f)

g = random.choice("巨匠電腦")  # 取得某一個字
print(g)

h = random.uniform(1.1, 5.4) # 1.1~5.4取值 float
print(h)

i = random.randrange(0, 100, 5)  # 間隔 5 取值
print(i)

print(5&3)
print(5|3)
print(5^3)



