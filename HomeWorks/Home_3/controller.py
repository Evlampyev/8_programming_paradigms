import sys

from human import Human
from computer import Computer
from board import Board
from view import View
from time import sleep


class Controller:

    def __init__(self):
        self.gamers = []
        new_view = View()
        menu_choose = new_view.menu_choose


        match menu_choose:
            case '1':
                name_1 = new_view.get_name()
                first_player = Human(name_1)
                name_2 = View.get_name()
                second_player = Human(name_2, '0')
            case '2':
                name_1 = new_view.get_name()
                first_player = Human(name_1)
                second_player = Computer('0')
            case '3':
                first_player = Computer()
                second_player = Computer('0')
            case _:
                sys.exit()
        size = new_view.size
        self.gamers.append(first_player)
        self.gamers.append(second_player)

        self.board = Board(size)
        new_view.print_gamers(self.gamers)
        new_view.print_board(self.board)

        motion = 0
        now_figure = '-'
        while not self.board.victory(now_figure) and self.board.size * self.board.size != motion:
            now_play = self.gamers[motion % 2]
            now_figure = now_play.figure
            if type(now_play).__name__ == 'Human':
                step = new_view.human_step(now_play.name, self.board.all_step)
            else:
                step = now_play.new_step(self.board.size, self.board.all_step)
                new_view.computer_step(now_play.name, step)
                sleep(1)

            self.board.all_step.add(step)
            self.board.change(step, now_play.figure)
            new_view.print_board(self.board)
            motion += 1
            # now_play = self.gamers[motion % 2]
        if self.board.victory(now_figure):
            new_view.congratulation(now_play)
        else:
            new_view.parity()
