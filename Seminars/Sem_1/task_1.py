# Декларативный стиль:

def decl_calc_factorial(n):
    if n == 0:
        return 1
    return n * decl_calc_factorial(n - 1)


# Императивный стиль:

def imper_calc_fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


# *******************************

# Императивный стиль:

def imper_check_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5 + 1)):
        if number % i == 0:
            return False
    return True


# Декларативный стиль

def decl_is_prime(number):
    gen_list = (i for i in range(2, int(number * 0.5) + 1))  #генератор списка,
                                                            # в памяти хранится первое и алгоритм поиска следующего
    if number < 2:
        return False
    list_of_bool = map(lambda x: number % x != 0, gen_list)
    return all(list_of_bool)
