# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением 
# дробной части элементов.
# Пример:
# o [1.1, 1.2, 3.1, 5, 10.01] => 0.19

data = [1.1, 1.2, 3.1, 5, 10.01]
# for i in range(len(data)):
#     quotient = int(data[i] // 1)
#     item = round(data[i] - quotient, 2)
#     data[i] = item
data = list(map(lambda x: round(x - int(x // 1), 2), data)) # Примернены lambda-функция и map 
min = data[0]
max = data[0]
print(data)
for i in range(1, len(data)):
    if data[i] != 0 and data[i] < min:
        min = data[i]
    if data[i] != 0 and data[i] > max:
        max = data[i]
print(round(max - min, 3))