# Написать классы, которые будут использованы как счета в банке. Каждый счет - в своей валюте. Соответственно, у каждого объекта счета должны быть атрибуты с суммой денег, хранящихся на нём, и название кошелька. Каждый класс счета должен в себе хранить коэффициент отношения стоимости своей валюты к базовой валюте.

# Нам понадобится один базовый класс BaseWallet, в котором будут реализованы общие для всех валютных счетов методы, и три класса для конкретных валютных счетов: RubbleWallet, DollarWallet, EuroWallet. Будем считать коэффициентами отношения валют к базовой валюте:

# Рубль: 1
# Доллар: 60
# Евро: 70
# Протокол взаимодействия объектов следующий:

# RubbleWallet("Первый кошелек", 10), где "Первый кошелек" - это название кошелька, а 10 - сумма денег на нём.
# аналогичные конструкторы для других счетов
# RubbleWallet("X", 10) + 20 == RubbleWallet("X", 30) - при сложении с числом считаем, что это та же валюта.
# RubbleWallet("X", 10) += 20 - должен поддерживаться и такой синтаксис
# 20 + RubbleWallet("X", 10) == RubbleWallet("X", 30) - radd для чисел
# RubbleWallet("X", 20) + DollarWallet("D", 10) == RubbleWallet("X", 620) - конвертация валюты при сложении счетов.
# DollarWallet("D", 2) + RubbleWallet("X", 60) == DollarWallet("D", 3) - результат - в валюте первого слагаемого.
# DollarWallet("D", 2) += RubbleWallet("X", 60) - здесь тоже должен поддерживаться этот синтаксис.
# предыдущие 6 пунктов реализовать и для вычитания
# RubbleWallet("X", 10) * 20 == RubbleWallet("X", 200) - умножение на число
# RubbleWallet("X", 10) *= 20 - тоже с таким синтаксисом
# те же 2 пункта для деления
# 20 * RubbleWallet("X", 10) == RubbleWallet("X", 200) - умножение числа на кошелек
# DollarWallet("A", 15) == DollarWallet("B", 15): два объекта равны, если у них совпадает тип кошелька и сумма на счете.
# RubbleWallet("X", 100).spend_all() - для любого типа кошелька релизовать функцию, которая обнуляет баланс, если он положительный
# DollarWallet("X", 1).to_base() == 60 - эта функция должна возвращать число денег в кошельке в базовой валюте
# print(DollarWallet("Q", 150)) - должна выводить строку: 'Dollar Wallet Q 150' (и аналогично Rubble и Euro для остальных кошельков)
# У каждого объекта должны быть доступны атрибуты:

# name - название кошелька
# amount - количество денег на счете
# exchange_rate - коэффициент стоимости валюты к базовой


class BaseWallet:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.exchange_rate = 1
        self.base_rate = 1 / self.exchange_rate

    def __add__(self, other):   
        if isinstance(other, BaseWallet) or issubclass(type(other), BaseWallet):
            self.amount += other.amount * (other.exchange_rate/self.exchange_rate)
        else: 
            self.amount += float(other)
        return self

    def __iadd__(self, other):   
        if isinstance(other, BaseWallet) or issubclass(type(other), BaseWallet):
            self.amount += other.amount * (other.exchange_rate/self.exchange_rate)
        else: 
            self.amount += float(other)
        return self
    
    def __radd__(self, other):   
        self.amount += float(other)
        return self

    def __sub__(self, other):   
        if isinstance(other, BaseWallet) or issubclass(type(other), BaseWallet):
            self.amount -= other.amount * other.exchange_rate
        else: 
            self.amount -= float(other)
        return self

    def __isub__(self, other):   
        if isinstance(other, BaseWallet)  or issubclass(type(other), BaseWallet):
            self.amount -= other.amount * other.exchange_rate
        else: 
            self.amount -= float(other)
        return self
    
    def __rsub__(self, other):   
        self.amount -= float(other)
        return self

    def __mul__(self, other):   
        if isinstance(other, BaseWallet) or issubclass(type(other), BaseWallet):
            self.amount *= other.amount * other.exchange_rate
        else: 
            self.amount *= float(other)
        return self

    def __imul__(self, other):   
        if isinstance(other, BaseWallet)  or issubclass(type(other), BaseWallet):
            self.amount *= other.amount * other.exchange_rate
        else: 
            self.amount *= float(other)
        return self
    
    def __rsub__(self, other):   
        self.amount *= float(other)
        return self

    def __truediv__(self, other):   
        if isinstance(other, BaseWallet)  or issubclass(type(other), BaseWallet):
            self.amount /= other.amount * other.exchange_rate
        else: 
            self.amount /= float(other)
        return self

    def __itruediv__(self, other):   
        if isinstance(other, BaseWallet) or issubclass(type(other), BaseWallet):
            self.amount /= other.amount * other.exchange_rate
        else: 
            self.amount /= float(other)
        return self
    
    def __eq__(self, other):
        return type(self) == type(other) and self.amount == other.amount

    def __str__(self):
        return '{} {} {}'.format(self.__class__.__name__ ,self.name, self.amount)

    def spend_all(self):
        if self.amount > 0: self.amount = 0
    
    def to_base(self):
        return self.amount * self.base_rate

class RubbleWallet(BaseWallet):
    def __init__(self, name, amount):
       super().__init__(name, amount)
       self.exchange_rate = 1
       self.base_rate = 1 / self.exchange_rate

class DollarWallet(BaseWallet):
    def __init__(self, name, amount):
       super().__init__(name, amount)
       self.exchange_rate = 60
       self.base_rate = 1 / self.exchange_rate

class EuroWallet(BaseWallet):
    def __init__(self, name, amount):
       super().__init__(name, amount)
       self.exchange_rate = 70
       self.base_rate = 1 / self.exchange_rate

wal = RubbleWallet('x',10)
print(wal)
wal += 10
print(wal)
wal += RubbleWallet('x',10)
print(wal)
print(25 + wal)
wal2 = RubbleWallet('x',10)
print(wal2)
wal2 -= 1
print(wal2)
wal2 -= RubbleWallet('x',8)
print(wal2)
print(RubbleWallet('x',10) == RubbleWallet('y',10))
print(RubbleWallet('x',10) == RubbleWallet('y',11))
wal3 = DollarWallet('b', 10)
wal3 += 10
print(wal3)
wal3 += RubbleWallet('x',60)
print(wal3)
print(RubbleWallet('x',60)+DollarWallet('b', 10))
print(wal3.to_base())
wal3.spend_all()
print (wal3)

