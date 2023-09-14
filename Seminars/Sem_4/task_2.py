from random import randint
from typing import List


def normlization(lst: List[int]) -> List[float]:  # Маленький лист не читается в Python 3.7 и ниже
    x_min = min(lst)
    x_max = max(lst)
    return list(map(lambda x: round((x - x_min) / (x_max - x_min), 2), lst))


array = []
for i in range(10):
    array.append(randint(0, 15))
print(array)
print(normlization(array))
