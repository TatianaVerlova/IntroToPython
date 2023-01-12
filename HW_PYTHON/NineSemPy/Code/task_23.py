# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o [2, 3, 4, 5, 6] => [12, 15, 16];
# o [2, 3, 5, 6] => [12, 15]


def sum_of_pairs(lst):
    result = [lst[i] * lst[(i + 1) * (-1)] for i in range(len(lst) // 2)]
    if len(lst) % 2:
        item = lst[len(lst) // 2] ** 2
        result.append(item)
    return result


lst1 = [2, 3, 4, 5, 6]
lst2 = [2, 3, 5, 6]
print(sum_of_pairs(lst1))
print(sum_of_pairs(lst2))
