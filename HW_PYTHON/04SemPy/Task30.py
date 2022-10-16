# 30). Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141 10^(-1) ≤ d ≤ 10^(-10)

import math
str_pi = str(math.pi)
d = float(input('Введите d: '))
digit = 0
while d < 1:
    digit += 1
    d *= 10
print(float(str_pi[0:digit+2]))

