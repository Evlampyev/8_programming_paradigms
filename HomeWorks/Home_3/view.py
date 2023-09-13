from board import Board
from gamer import Gamer
from log import Logger


class View:
    def __init__(self):
        self.menu_choose = self.greeting()
        if self.menu_choose in '123':
            self.size = self.choosing_size()
        path = 'log.txt'
        self.logger = Logger(path)

    @staticmethod
    def get_name() -> str:
        """
        Получение имени игрока
        :return: name: str
        """
        name = input("Введите ваше имя: ")
        return name

    @staticmethod
    def greeting() -> str:
        """
        Выбор участников игры
        :return: gamer : str
        """
        print("Кто будет играть?")
        print("1. Человек с человеком")
        print("2. Человек с компьютером")
        print("3. Компьютер с компьютером")
        print("4. Выход")
        gamer = input("Ваш выбор: ")
        return gamer

    @staticmethod
    def choosing_size() -> int:
        """
        Определение размера поля s*s
        :return: size: int
        """
        correct = False
        while not correct:
            try:
                size = int(input("Укажите количество строк на поле (рекомендую 3-7): "))
                if 2 <= size <= 7:
                    correct = True
            except ValueError:
                print("При вводе учитывайте рекомендации")
        return size

    def human_step(self, name: str, all_step: set):
        correct = False
        while not correct:
            try:
                st = int(input(f"Ваш ход, {name}, (число от 0 до {self.size * self.size - 1}): "))
                if 0 <= st <= self.size * self.size - 1:
                    if st not in all_step:  # проверка на свободные ячейки
                        correct = True
                    else:
                        print('Эта ячейка уже занята')
            except ValueError:
                print(f"Введите число от 0 до {self.size * self.size - 1}:")
        data = f"{name} ходит {st}\n"
        self.logger.write_log(data)
        return st

    def computer_step(self, name, step):
        data = f"{name} ходит: {step}\n"
        print(data)
        self.logger.write_log(data)

    def print_board(self, board: Board):
        """
        Печать игрового поля
        :param board: игровое поле
        :return:
        """
        print(board)

    def print_gamers(self, players: list[Gamer]):
        data = "---  Играют  --- \n"
        data += f'Первый игрок: {players[0].name}, ходит {players[0].figure} \n'
        data += f'Второй игрок: {players[1].name}, ходит {players[1].figure} \n'
        print(data)
        self.logger.write_log(data)

    def congratulation(self, player: Gamer):
        data = f'Поздравляем {player.name} - победил(а)\n'
        print(data)
        self.logger.write_log(data)

    @staticmethod
    def parity():
        print('Ничья')
