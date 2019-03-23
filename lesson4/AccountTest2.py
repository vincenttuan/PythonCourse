class Account:
    __name = ''
    __balance = 0

    def __init__(self, name, balance):
        self.__name = name
        self.__balance += balance

    def setBalance(self, balance):
        if balance >= 0:
            self.__balance += balance

    def getBalance(self, password):
        if password == '1234':
            return self.__balance

    def getName(self):
        return self.__name;


account = Account('John', 3000)
print(account.getName())
print(account.getBalance('1234'))
