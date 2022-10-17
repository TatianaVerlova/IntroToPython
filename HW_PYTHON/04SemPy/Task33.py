# 33). Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать 
# в файл многочлен степени k и приравняйте его к нулю.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# 2*x**2 + 4*x + 5 = 0
# или
# 2*x^2 + 4*x + 5 = 0

import random
from random import randint

k = int(input('Введите k: '))
max_coef = 9
coefficients = []
for i in range(k+1):
    if i == 0:
        coefficients.append(randint(1, max_coef))
    else:
        coefficients.append(randint(0, max_coef))

polynomial = []
for i in coefficients:
    if i == 0:
        k -= 1
    elif k == 0:
        polynomial.append(f'{i}')
        break
    elif k == 1:
        if i == 1:
            polynomial.append(f'x')
            k -= 1
        else:
            polynomial.append(f'{i}x')
            k -= 1
    elif i == 1:
        polynomial.append(f'x^{k}')
        k -= 1
    else:
        polynomial.append(f'{i}x^{k}')
        k -= 1
with open('Task33.txt', 'w') as data:
    for i in range(len(polynomial)):
        if i != len(polynomial) - 1:
            data.write(f'{polynomial[i]} + ')
        else:
            data.write(f'{polynomial[i]} = 0')