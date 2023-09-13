from gamer import Gamer


class Human(Gamer):

    def __init__(self, name, figure='+'):
        self.figure = figure
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, value: str):
        self.name = value


