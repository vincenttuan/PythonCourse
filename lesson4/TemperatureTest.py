#攝氏 = 5/9 乘 (華氏溫度 - 32)
#華氏 = (攝氏)(9/5) + 32

class Celsius: # 攝氏
    #def get(self, f):
    #    return 5 / 9 * (f-32)

    def __get__(self, instance, owner):
        return 5 / 9 * (instance.fahrenheit - 32)

    def __set__(self, instance, value):
        instance.fahrenheit = value * 9 / 5 + 32

class Temperature: # 溫度
    celsius = Celsius()
    def __init__(self, f):
        self.fahrenheit = f # fahrenheit = 華氏

t = Temperature(32)
print(t.celsius) # __get__
t.celsius = 100 # __set__
print(t.fahrenheit)


