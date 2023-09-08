# Процедурный стиль реализации
# Сумма элементов главной диагонали матрицы

from random import randint


def get_matrix(N: int) -> list[list]:
    """
    Создание матрицы
    :param N: Количество элементов в строке
    :return: Матрица N*N
    """
    return [[randint(1, 10) for i in range(N)] for j in range(N)]


def print_matrix(matrix: list[list]) -> None:
    """
    Печать матрицы
    :param matrix: Матрица
    :return: None
    """
    print("Исходная матрица: ")
    for i, row in enumerate(matrix):  # enumerate - возвращает не только элемент, но и его индекс
        for j, el in enumerate(row):
            print(f"{el:2.0f}", end=" ")
        print()


def get_step(matrix: list[list]) -> int:
    """
    Сумма элементов главной диагонали
    :param matrix: матрица
    :return: Сумма элементов
    """
    step = 0
    for i, row in enumerate(matrix):  # enumerate - возвращает не только элемент, но и его индекс
        for j, el in enumerate(row):
            if i == j:
                step += el
    return step


if __name__ == "__main__":
    n = 5  # Размер матрицы
    matr = get_matrix(n)
    print_matrix(matr)
    matrix_step = get_step(matr)
    print(f"След матрицы: {matrix_step}")
