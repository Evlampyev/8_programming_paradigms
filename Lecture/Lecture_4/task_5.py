# Сумма квадратов: Python
# Вход: список с целыми числами
# Задача: возвести все числа в квадрат и вернуть их сумму (сумму квадратов)

def sum_squares(lst: list) ->int:
    return sum(map(lambda x: x**2, lst))


print(sum_squares([1,2,3]))
