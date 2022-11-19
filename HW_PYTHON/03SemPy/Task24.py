# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# o [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 5, 10.01]
for i in range(len(lst)):
    quotient = int(lst[i] // 1)
    item = round(lst[i] - quotient, 2)
    lst[i] = item
min = lst[0]
max = lst[0]
print(lst)
for i in range(1, len(lst)):
    if lst[i] != 0 and lst[i] < min:
        min = lst[i]
    if lst[i] != 0 and lst[i] > max:
        max = lst[i]
print(round(max - min, 3))