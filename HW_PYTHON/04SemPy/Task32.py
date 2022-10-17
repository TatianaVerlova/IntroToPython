# 32). Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной 
# последовательности.

list = [15, 10, 15, 11, 12, 15, 13, 15, 13]
new_list = []
repeating = []
while list:
    item = list.pop()
    if not(item in list) and not(item in repeating):
        new_list.append(item)
    else:
        repeating.append(item)
print(new_list)