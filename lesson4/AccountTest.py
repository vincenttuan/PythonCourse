class Account:
    name = ''
    __balance = 0

    def setBalance(self, balance):
        if balance >= 0:
            self.__balance += balance

    def getBalance(self, password):
        if password == '1234':
            return self.__balance


account = Account()
account.name = 'Vincent'
account.setBalance(10000)
print(account.getBalance('1234'))
account.setBalance(500)
print(account.getBalance('1234'))
account.setBalance(-900)
print(account.getBalance('1234'))
print(account.getBalance('12345'))
