from board import Board
from gamer import Gamer


class View:
    def __init__(self):
        self.menu_choose = self.greeting()
        self.size = self.choosing_size()

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
        size = int(input("Укажите количество строк на поле: "))
        return size

    def human_step(self, name):
        st = int(input(f"Ваш ход, {name}, (число от 0 до {self.size * self.size - 1}): "))
        return st

    def computer_step(self, name, step):
        print(f"{name} ходит: {step}")

    def print_board(self, board: Board):
        """
        Печать игрового поля
        :param board: игровое поле
        :return:
        """
        print(board)

    def print_gamers(self, players: list[Gamer]):
        print("---  Играют  --- ")
        print(f'Первый игрок: {players[0].name}, ходит {players[0].figure}')
        print(f'Второй игрок: {players[1].name}, ходит {players[1].figure}')

    @staticmethod
    def congratulation(player: Gamer):
        print(f'Поздравляем {player.name} - победил')

    @staticmethod
    def parity():
        print('Ничья')
