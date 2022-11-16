class Lada:
    #атрибуты класса 
    n_of_wheels = 4
    rule = 1

    def __init__(self, color, engine): # встроенный метод. Под капотом вызывается конструктор объекта этого класса. 
# Мы в данном случае перегружаем встроенный метод
        self.color = color
        self.engine = engine

    def method(self):
        print(Lada.rule)
        print(self.rule)
        self.rule = 2
        print(Lada.rule)
        print(self.rule)
        print(self.color)