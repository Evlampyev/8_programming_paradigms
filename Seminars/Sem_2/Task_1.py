# структурная реализация
# Сумма элементов главной диагонали матрицы

from random import randint

N = 5  # Размер матрицы
matrix = [[randint(1, 10) for i in range(N)] for j in range(N)]
print("Исходная матрица: ")
matrix_step = 0
for i, row in enumerate(matrix):  # enumerate - возвращает не только элемент, но и его индекс
    for j, el in enumerate(row):
        print(f"{el:2.0f}", end=" ")
        if i == j:
            matrix_step += el
    print()
print(f"След матрицы: {matrix_step}")
