from typing import List
from random import randint


def mse(lst1: List[int], lst2: List[int]) -> float:
    summ = 0
    assert len(lst1) == len(lst2), "Списки не совпадают"
    for i in range(len(lst1)):
        summ += (lst1[i] - lst2[i]) ** 2
    return summ / len(lst1)


def mse_2(arr1: List[int], arr2: List[int]) -> float:
    sum_diff_x_y = sum(map(lambda x, y: (x - y) ** 2, arr1, arr2))
    return round(sum_diff_x_y / len(arr1), 2)


def main():
    lst_1 = []
    lst_2 = []
    for i in range(10):
        lst_1.append(randint(0, 10))
        lst_2.append(randint(0, 10))
    print(f"Array_1: {lst_1}\nArray_2: {lst_2}")
    print(f"MSE = {mse(lst_1, lst_2)}")


if __name__ == "__main__":
    main()
