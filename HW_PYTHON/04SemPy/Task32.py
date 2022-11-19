# 32). Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной 
# последовательности.

lst = [15, 10, 15, 11, 12, 15, 13, 15, 13]
new_lst = []
repeating = []
while lst:
    item = lst.pop()
    if not(item in lst) and not(item in repeating):
        new_lst.append(item)
    else:
        repeating.append(item)
print(new_lst)