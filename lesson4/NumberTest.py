class Number:
    __n = 0

    def __add__(self, n):
        self.__n = self.__n + n

    def __sub__(self, n):
        self.__n = self.__n - n

    def __str__(self):
        return " n = " + str(self.__n)


number = Number()
number + 5 # 呼叫 __add__(4)
number - 2 # 呼叫 __sub__(2)
print(number)

