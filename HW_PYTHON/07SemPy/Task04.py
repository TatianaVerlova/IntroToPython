"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
class Car:
    speed = None
    color = None
    name = None
    is_police = None

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print("Скорость превышена!")
        else:
            print(self.speed)

class SportCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

class WorkCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print("Скорость превышена!")
        else:
            print(self.speed)

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

car_1 = Car(90, 'grey', 'Lada', False)
print(f'Скорость авто: {car_1.speed}; цвет: {car_1.color}; имя: {car_1.name}; полицейская: {car_1.is_police}')
car_1.go()
car_1.stop()
car_1.turn('направо')
car_1.show_speed()

car_2 = TownCar(70, 'white', 'KIA')
print(f'Скорость авто: {car_2.speed}; цвет: {car_2.color}; имя: {car_2.name}; полицейская: {car_2.is_police}')
car_2.go()
car_2.stop()
car_2.turn('налево')
car_2.show_speed()
car_2.speed = 50
car_2.show_speed()

car_3 = SportCar(120, 'red', 'Ferrari')
print(f'Скорость авто: {car_3.speed}; цвет: {car_3.color}; имя: {car_3.name}; полицейская: {car_3.is_police}')
car_3.go()
car_3.stop()
car_3.turn('направо')
car_3.show_speed()

car_4 = WorkCar(60, 'black', 'Mersedes')
print(f'Скорость авто: {car_4.speed}; цвет: {car_4.color}; имя: {car_4.name}; полицейская: {car_4.is_police}')
car_4.go()
car_4.stop()
car_4.turn('налево')
car_4.show_speed()
car_4.speed = 38
car_4.show_speed()

car_5 = PoliceCar(80, 'blue', 'Ford')
print(f'Скорость авто: {car_5.speed}; цвет: {car_5.color}; имя: {car_5.name}; полицейская: {car_5.is_police}')
car_5.go()
car_5.stop()
car_5.turn('направо')
car_5.show_speed()