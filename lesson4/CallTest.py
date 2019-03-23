class Entity:

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __call__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return str(self.x + self.y)


e = Entity(10, 20) # __init__
print(e)

e.x = 30
e.y = 40
print(e)

e.x, e.y = 50, 60
print(e)

e(70, 80) # __call__
print(e)



