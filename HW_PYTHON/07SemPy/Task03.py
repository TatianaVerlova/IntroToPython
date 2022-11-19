"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку __str__
__str__(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""
class Worker:
    name = None
    surname = None
    position = None
    _income = \
        {
            'wage': None,
            'bonus': None
        }

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus

    def __str__(self):
        salary = self._income['wage'] + self._income['bonus']
        return str(self.name + ' ' + self.surname + ', ' + self.position + ', ' + str(salary))

class Position(Worker):
    def __init__(self, position):
        self.position = position

    def get_full_name(self):
        full_name = input('Введите имя и фамилию сотрудника: ').split()
        self.name = full_name[0]
        self.surname = full_name[1]

    def get_total_income(self, wage, bonus):
        self._income['wage'] = wage
        self._income['bonus'] = bonus
        total_income = self._income['wage'] + self._income['bonus']
        return total_income

manager = Position('менеджер')
manager.get_full_name()
manager_total_income = manager.get_total_income(70000, 30000)
print(manager)
print(f'Имя сотрудника: {manager.name} {manager.surname}, его должность: {manager.position}, зарплата: {manager_total_income}')
