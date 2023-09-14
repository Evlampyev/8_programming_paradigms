def filter_by_age(people, age):
    # filtered_people = filter(lambda x: x['age'] > age, people)        # работает если поле age есть точно у всех записей
    filtered_people = filter(lambda x: x.get('age', -1) > age, people)  # get - позволяет избежать ошибки
                                                                        # если будет запись без поля "age"
                                                                        # -1 - это то, значение, которое будет браться,
                                                                        # если не будет найдено значение поле age
    return len(list(filtered_people))


def filter_by_age_1(people, age):
    return sum(map(lambda x: x.get('age', -1) > age, people))   # лямбда возвращает единицы и из можно суммировать


people = [
    {'name': 'Alla', 'age': 25},
    {'name': 'Ivan', 'age': 40},
    {'name': 'Vika', 'age': 35},
    {'name': 'Julia', 'age': 30},
    {'name': 'Petr'}

]

count = filter_by_age(people, 30)
print(count)

print(filter_by_age_1(people, 30))