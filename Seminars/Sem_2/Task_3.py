# Перевод числа из десятично системы счисления в любую другую
# Процедурный стиль
from string import ascii_uppercase, digits


def in_another_system(num: int, ansys: int = 2) -> str:
    """
    Перевод числа num из десятичной в sys
    :param num: исходное число
    :param ansys: основание другой системы счисления
    :return: строка в СС ansys
    """
    result = []
    # all_digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    all_digits = digits + ascii_uppercase # все цифры и заглавные буквы, чтобы их не набирать
    while num > 0:
        result.append(str(all_digits[num % ansys]))
        num = num // ansys
    return ''.join(reversed(result))


if __name__ == "__main__":
    N = 10
    for i in range(2, 16):
        print(f"{N} = {in_another_system(N, i)} в системе счисления {i} ")
