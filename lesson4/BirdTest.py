class Bird:
    def move(self):
        print('飛')


class Eagle(Bird):
    pass


class Ostrich(Bird):
    def move(self):
        print('跑')


bird = Bird()
bird.move()
eagle = Eagle()
eagle.move()
ostrich = Ostrich()
ostrich.move()
