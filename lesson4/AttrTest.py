# 建立動態屬性
class Book(object):
    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)

    def __getattr__(self, name):
        try:
            return object.__getattribute__(name)
        except:
            return name + ' is not found!'

    def __str__(self):
        return self.name + ' price : ' + str(self.price)


c = Book()
c.name = 'Python'
c.price = 180
print(c.name)
print(c.price)
print(c)
c.author = 'Vincent'
print(c.author)

print(c.company)