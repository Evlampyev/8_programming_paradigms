# Чистая функция:

def pow(x, y):
    return x ** y


# Не чистая функция:

def pow(x, y):
    print(x, y)
    return x ** y
