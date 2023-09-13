from abc import ABC
from math import pi as PI, sqrt


class Shape(ABC):
    def __init__(self):
        raise TypeError("Creaing instance of abstract class")

    def get_area(self):
        raise TypeError("Calling abstract method")  # вызов исключения при создании абстрактного класса

    def get_perimetr(self):
        raise TypeError("Calling abstract method")  # вызов исключения при создании абстрактного класса


class Triangle(Shape):
    def __init__(self, a, b, c):

        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        if not hasattr(self, 'perimetr'):
            p = self.get_perimetr() / 2
        else:
            p = self.perimetr / 2
        self.area = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return self.area

    def get_perimetr(self):
        self.perimetr = self.a + self.b + self.c
        return self.perimetr


class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def get_area(self):
        self.area = PI * self.radius * self.radius #лучше использовать умножение,
                                                    # чем возведение во 2 степень
        return self.area

    def get_perimetr(self) -> str:
        """
        Нахождение длины окружности
        :return: длина окружности
        """
        self.perimetr = 2 * PI * self.radius
        return f'{self.perimetr:0.4f}'


def get_area(obj: Shape):  # функция, которая передаёт площадь любого объекта одной "кнопкой"
    return obj.get_area()


if __name__ == "__main__":
    a = Triangle(3, 4, 5)
    print(a.get_area())
    print(a.get_perimetr())

    b = Circle(10)
    print(f"Площадь круга{b.get_area()}")
    print(f"Периметр круга: {b.get_perimetr()}")

    c = Triangle(4, 5, 6)
    d = Circle(5)

    print(get_area(c))
    print(get_area(d))
