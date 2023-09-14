# Каррирование (Дробление на подшаги)

# До каррирования
def add(x, y):
    return x + y


add(3, 5)


# После каррирования
def add(x):
    def add_x(y):
        return x + y

    return add_x


add(3)(5)
