from abc import ABC


class Gamer(ABC):

    def __init__(self, name='Игрок_1', figure='+'):
        self.name = name
        self.figure = figure

    def new_step(self):
        """
        Новый ход
        :return:
        """
        pass


