class Bird:
    def move(self):
        print('飛')

    def play(self):
        print('玩')

class Eagle(Bird):
    pass


class Ostrich(Bird):
    def move(self):
        print('跑')


def move(bird):
    bird.move()
    bird.play()


bird_list = [Bird(), Eagle(), Ostrich()]
for bird in bird_list:
    move(bird)

