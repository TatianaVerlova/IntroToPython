"""
Задание 1.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init()__),
который должен принимать данные (список списков) для формирования матрицы.
[[], [], []]
Следующий шаг — реализовать перегрузку метода __str()__ для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add()__ для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
Пример:
1 2 3
4 5 6
7 8 9
1 2 3
4 5 6
7 8 9
Сумма матриц:
2 4 6
8 10 12
14 16 18
"""

class Matrix:
    lst = None

    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        string = ''
        for el in self.lst:
            for item in el:
                string += str(item) + ' '
            string += '\n'
        return string

    def __add__(self, other):
        matrix_sum = []
        for i in range(0, len(self.lst)):
            matrix_element = []
            for j in range(0, len(self.lst[i])):
                value = self.lst[i][j] + other.lst[i][j]
                matrix_element.append(value)
            matrix_sum.append(matrix_element)
        return matrix_sum

matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print('matrix1:\n')
print(matrix1)
print()
print('matrix2:\n')
print(matrix2)
print()
print('Сумма двух матриц:\n')
print(matrix1 + matrix2)