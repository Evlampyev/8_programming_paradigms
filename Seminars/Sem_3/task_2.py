# Как правильно писать сеттеры и гетеры
class A:
    line = 55

    @property  # декоратор для печати
    def l(self):
        return self.line

    @l.getter  # декоратор для получения значения
    def l(self):
        return self.line

    @l.setter  # декоратор для установки значения, если я не хочу, чтобы значение можно установить, то его закоментировать или не писать
    def l(self, value):
        if isinstance(value, int) and value > 0:  # если тип данных инт и больше 0
            self.line = value


a = A()
a.l = 13  # если сеттера нет, то это не сработает
print(a.l)
