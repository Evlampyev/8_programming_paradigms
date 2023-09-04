from random import randint


def sort_list_imperative(numbers):
    # Императивный код
    return numbers


def sort_list_declarative(numbers):
    # Декларативный код
    return sorted(numbers, reverse=True)


lst = [randint(-10, 10) for i in range(10)]
print(f"Исходный: {lst}")

print(f"Императивный: {sort_list_imperative(lst)}")
print(f"Декларативный: {sort_list_declarative(lst)}")
