# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# o [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(len(list)):
    quotient = int(list[i] // 1)
    item = round(list[i] - quotient, 2)
    list[i] = item
min = list[0]
max = list[0]
print(list)
for i in range(1, len(list)):
    if list[i] != 0 and list[i] < min:
        min = list[i]
    if list[i] != 0 and list[i] > max:
        max = list[i]
print(round(max - min, 3))