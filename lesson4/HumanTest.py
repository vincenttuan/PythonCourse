class Human:
    name = ''
    age = 0
    sex = ''

    def __str__(self):
        return self.name + ',' + str(self.age) + ',' + self.sex


human = Human()
human.name = 'Vincent'
human.age = 20
human.sex = '男'

print(human)
print(human.name)
print(human.age)
print(human.sex)
