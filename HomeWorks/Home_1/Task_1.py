from random import randint, choice
from time import perf_counter


def sort_list_imperative(numbers):
    for i in range(len(numbers) - 1):
        for j in range(1, len(numbers) - i - 1):
            if numbers[j - 1] < numbers[j]:
                numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
    return numbers


def sort_list_declarative(numbers: list[int]):
    # Декларативный код. Метод Хоара
    if len(numbers) > 1:
        pivot = choice(numbers)
        less = [num for num in numbers if num < pivot]
        more = [num for num in numbers if num > pivot]
        equal = [num for num in numbers if num == pivot]
        return sort_list_declarative(more) + equal + sort_list_declarative(less)
    else:
        return numbers


def sort_list_declarative_in(numbers):
    # Декларативный код встроеннными средствами
    return sorted(numbers, reverse=True)


def main():
    lst = [randint(-10000, 10000) for i in range(1000)]
    print(f"Исходный: {lst}")
    time1 = perf_counter()
    print('*' * 10)
    print(f"Императивный: {sort_list_imperative(lst)}")
    time2 = perf_counter()

    print(f"Декларативный: {sort_list_declarative(lst)}")
    time3 = perf_counter()

    print(f"Декларативный встроенный: {sort_list_declarative_in(lst)}")
    time4 = perf_counter()

    print(f"    Time imper: {time2 - time1:0.5f}")
    print(f"    Time declar: {time3 - time2:0.5f}")
    print(f"    Time in_declar: {time4 - time3:0.5f}")


if __name__ == "__main__":
    main()
