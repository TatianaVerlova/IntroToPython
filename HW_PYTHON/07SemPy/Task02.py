"""
Задание 2.
Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами.
Проверить работу метода.
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""
class Road:
    _length = None
    _width = None
    asphalt_m = None
    asphalt_d = None

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt(self, asphalt_mass, asphalt_depth):
        self.asphalt_m = asphalt_mass
        self.asphalt_d = asphalt_depth
        asphalt_coating = self._length * self._width * self.asphalt_m * self.asphalt_d
        return asphalt_coating

data = input('Введите длину и ширину дороги в м через пробел: ').split()
length_1 = int(data[0])
width_1 = int(data[1])
road_1 = Road(length_1, width_1)
print(f'Для покрытия всего дорожного полотна необходимо {road_1.asphalt(25, 0.05)} кг асфальта')

