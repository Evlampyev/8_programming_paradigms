from random import randint
from typing import List
from time import time


def buble_sort(lst: List[int]) -> List[int]:
    """
    Сортировка пузырьком
    :param lst: исходный список
    :return: отсортированный список
    """
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst


def merge_sorting(lst: List[int]):
    """
    Сортировка слиянием
    :param lst: исходный список
    :return:
    """
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sorting(lst[:mid])
    right = merge_sorting(lst[mid:])
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Метод слияния двух списков
    :param left:
    :param right:
    :return: отсортированный список
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


def binary_search(lst: List[int], target: int) -> int:
    """
    Бинарный поиск в отсортированном списке
    :param lst: отсортированный список
    :param target: искомое значение
    :return: индекс элемента
    """
    result = None
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if lst[mid] == target:
            result = mid
            break
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result


def main():
    lst = [randint(1, 20) for _ in range(10)]
    print(f"До сортировки: {lst}")
    now = time()
    # print(now)
    print(buble_sort(lst))
    print(f"{time() - now : 4.8f}")
    now = time()
    merge_sorting_lst = merge_sorting(lst)
    print(merge_sorting_lst)
    print(f"{time() - now : 4.8f}")
    target = randint(0, 20)
    print(target)
    result = binary_search(merge_sorting_lst, target)
    if result is None:
        print("Такого числа нет")
    else:
        print(f"Искомое число:{target} стоит на {result}")


if __name__ == '__main__':
    main()
