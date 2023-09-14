from typing import List
from random import randint


def double_search(lst: List[int]) -> List[int]:  # решение не оптимально из-за count много прохождений по списку
    return list(set(filter(lambda x: lst.count(x) > 1, lst)))


def search_duplicates(arr):
    uniq_set = set()
    return list(set(filter(lambda x: x in uniq_set or uniq_set.add(x), arr)))


def search(arr):  # Более понятный и простой
    count_item = {}
    for item in arr:
        count_item.setdefault(item, 0)
        count_item[item] += 1
    return list(filter(lambda x: count_item[x] > 1, count_item))


data_list = [randint(0, 10) for i in range(10)]
print(data_list)
print(double_search(data_list))

duplicates = search_duplicates(data_list)
print(duplicates)

print((search(data_list)))
