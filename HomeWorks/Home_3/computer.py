from random import randint

from gamer import Gamer
from random import choice
from string import ascii_letters


class Computer(Gamer):

    def __init__(self, figure='+'):
        self.figure = figure
        self.set_name()

    def get_name(self):
        return self.name

    def set_name(self):
        name = ""
        for i in range(4):
            name += choice(ascii_letters)
        self.name = name

    def new_step(self, size, all_step):
        new = randint(0, size * size - 1)
        while new in all_step:
            new = randint(0, size * size - 1)
        return new


