# Императивный стиль
def search_number_imper(array: list[int], target: int) -> bool:
    for number in array:
        if number == target:
            return True
    return False


# Декларативный стиль
def search_number_decl(array: list[int], target: int) -> bool:
    return target in array


def search_decl(array: list[int], target: int, i=0, count=0):
    if i >= len(array):
        return count
    tmp = 0
    if isinstance(array[i], list):
        tmp = search_decl(array[i], target, i=0, count=0)
    if array[i] == target:
        count += 1
    return search_decl(array, target, i=i + 1, count=count + tmp)


lst = [1, 2, 3, 4, 5, 6]
tar = 5
print(search_number_decl(lst, tar))
print(search_number_imper(lst, tar))
print(search_decl(lst, tar))
