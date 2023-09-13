class Board:
    def __init__(self, size):
        self.size = size
        self.board = [['*'] * size] * size

    def __str__(self) -> str:
        """
        Возвращает строку - игровое поле
        :return:
        """
        res = '-' * (self.size + 2) + '\n'
        for i in range(self.size):
            for j in range(self.size):
                res += self.board[i][j] + " "
            res += "\n"
        res += '-' * (self.size + 2)
        return res

    def change(self, step: int, figure: str):
        """
        Внесение изменений в игровое поле
        :param step: в какую ячейку ходим от 0 до 8
        :param figure: кто ходит "+" или "0"
        :return: None
        """
        row = step // self.size
        col = step % self.size
        self.board[row][col] = figure

    def victory(self, figure) -> bool:
        """
        Проверка на победителя
        :return: "+" или "0" или "*"
        """
        result = False
        size = self.size
        for i in range(size):
            if self.board[i].count(figure) == size:
                result = True
                break
        if not result:
            temp1 = 0
            temp2 = 0
            for i in range(size):
                if self.board[i][i] == figure:
                    temp1 += 1
                if self.board[size - 1 - i][i] == figure:
                    temp2 += 1
            if temp1 == size or temp2 == size:
                result = True

        return result
