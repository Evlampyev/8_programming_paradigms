# Императивная парадигма
# Процедурный стиль

def multiplication_table(N: int) -> None:
    """
    Вывод таблицы умножения от 1 до 10 для одного числа
    :param N: Для какого числа таблица умножения
    :return: None
    """
    for i in range(1, 11):
        print(f"{N} * {i} = {N * i:2.0f}")


n = int(input("Введите n: "))
for j in range(1, n + 1):
    multiplication_table(j)
    print('____________')
