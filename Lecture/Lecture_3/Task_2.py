from math import sqrt, acos, degrees


class Rectangle:
    def __init__(self, width: int, length: int):
        self.width = width
        self.length = length

    def __str__(self):
        return f'Прамоугольник шириной {self.width} и длиной {self.length}'

    def get_square(self) -> int:
        """
        Возращает площадь прямоугольника
        :return: a*b
        """
        self.square = self.width * self.length
        return self.square

    def get_perimetr(self) -> int:
        """
        Возвращает периметр прямоугольника
        :return: (a+b)*2
        """
        self.perimetr = (self.width + self.length) * 2
        return self.perimetr

    def calc_diagonal_length(self) -> float:
        """
        Вычисление диагоналей
        :return: длина диагонали
        """
        self.diag = sqrt(self.length ** 2 + self.width ** 2)
        return self.diag

    def calc_diag_angles(self):
        """
        Вычесление двух углув между диагоналями прямоугольника
        :return: два угла в градусах
        """
        if not hasattr(self, 'diag'):  # Если нет аттрибута с именем diag
            self.calc_diagonal_length()
        cos_diag_length = self.length / self.diag
        angle_diag_length = acos(cos_diag_length)
        angle_diag_length = degrees(angle_diag_length)
        first_angle = 180 - (2 * angle_diag_length)
        second_angle = (360 - 2 * first_angle) / 2
        assert (
                       first_angle + second_angle) == 180  # формирует исключение (exeption) типа "assertion error" если условие вернет "False"
        return f"{first_angle:4.2f} и {second_angle:4.2f}"

    def __add__(self, other):
        if not hasattr(self, 'square'):
            self.get_square()
        if not hasattr(other, 'square'):
           other.get_square()
        return self.square + other.square

    def __eq__(self, other):
        return self.square == other.square


if __name__ == "__main__":
    first = Rectangle(3, 4)
    second = Rectangle(4, 5)
    print(first)
    print(f"Площадь: {first.get_square()}")
    print(f"Периметр: {first.get_perimetr()}")
    print(f"Длина диагонали: {first.calc_diagonal_length():4.2f}")
    print(f"Углы м/у диагоналями: {first.calc_diag_angles()} градусов")
    print(second)
    print(f"Площадь: {second.get_square()}")
    print(f"Периметр: {second.get_perimetr()}")
    print(f"Длина диагонали: {second.calc_diagonal_length():4.2f}")
    print(f"Углы м/у диагоналями: {second.calc_diag_angles()} градусов")
    print(first + second)
    print(first == second)
