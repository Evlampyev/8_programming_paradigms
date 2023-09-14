# функция композиции

def fun_1(x):
    return x + 10


def fun_2(x):
    return x ** 2


def compose(first, second):  # не возвращает значение, а возвращает функцию,
    # которую можно использовать
    return lambda x: first(second(x))


y = 3
print(compose(fun_1, fun_2)(y))
