class Engine:
    power = 0


class Wheel:
    count = 0


class Car(Engine, Wheel):
    name = ''

    def __init__(self, power, count, name) -> None:
        self.power = power
        self.count = count
        self.name = name

    def __str__(self) -> str:
        return str(self.power) + ", " + str(self.count) + ", " + self.name


car = Car(6000, 4, 'Motor')
print(car)




