# На вход подается целочисленный массив. Необходимо получить список, элементы которого - это остаток от
# деления соответствующего элемента в исходном массиве на 5

# структурный стиль:
array = [1, 2, 34, 5, 6, 7, 56, 3, 34, 5, 6]
new_list = []
for el in array:
    new_list.append(el % 5)

print(*new_list)

# Функциональный стиль:
#мой
array = [1, 2, 34, 5, 6, 7, 56, 3, 34, 5, 6]
new_list = [el % 5 for el in array]
print(*new_list)

#их
array = [1, 2, 34, 5, 6, 7, 56, 3, 34, 5, 6]
modulo = lambda x: x % 5
new_list = list(map(modulo, array))
print(*new_list)
