# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# o 1, 4, 8, 7, 5 -> 8
# o 78, 55, 36, 90, 2 -> 90

list = [78, 55, 36, 90, 2]
max = list[0]
for i in list:
    if max < i:
        max = i
        print (f'Максимальное число равно {max}')