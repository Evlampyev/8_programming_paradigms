from random import randint


# императивный стиль
def doli_imper(array: list[int]) -> tuple[float]:
    size = len(array)
    if size == 0:
        raise ValueError('Required not empty list.')
    positiv = 0
    nul = 0
    negativ = 0
    for num in array:
        if num < 0:
            negativ += 1
        elif num == 0:
            nul += 1
        else:
            positiv += 1
    return positiv / size, nul / size, negativ / size


# Декларативный стиль
def doli_decl(array: list[int]) -> tuple[float]:
    if len(array) == 0:
        raise ValueError('Required not empty list.')
    pos = list(filter(lambda x: (x > 0), array))
    nul = list(filter(lambda x: x == 0, array))
    neg = list(filter(lambda x: x < 0, array))
    return len(pos) / len(array), len(nul) / len(array), len(neg) / len(array)


lst = [randint(-10, 10) for i in range(10)]
print(lst)

print(f"Императивный  - {doli_imper(lst)}")
print(f"Декларативный - {doli_decl(lst)}")
