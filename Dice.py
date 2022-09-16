import random

#Random value generator


class Dice:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def roll(self):

        print(f'({self.x}, {self.y})')


Dice = Dice(random.randint(0, 5), random.randint(6, 10))
Dice.roll()

