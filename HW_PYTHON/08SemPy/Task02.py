"""
Задание 2.
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Единственный класс этого проекта — одежда (класс Clothes).
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактный класс для единственного класса проекта,
проверить на практике работу декоратора @property
Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_consumption(self):
        pass

    def __add__(self, other):
        return self.fabric_consumption + other.fabric_consumption


class Coat(Clothes):
    v = None

    def __init__(self, value):
        self.v = value

    @property
    def fabric_consumption(self):
        return round(self.v / 6.5 + 0.5, 2)


class Costume(Clothes):
    h = None

    def __init__(self, value):
        self.h = value

    @property
    def fabric_consumption(self):
        return round(2 * self.h + 0.3, 2)


print('Нужно сшить пальто')
my_coat = Coat(5)
print(f'Расход ткани на пальто = {my_coat.fabric_consumption}')
print()
print('Нужно сшить костюм')
my_costume = Costume(10)
print(f'Расход ткани на костюм = {my_costume.fabric_consumption}')
print()
print(f'Общий расход ткани = {my_coat + my_costume}')
