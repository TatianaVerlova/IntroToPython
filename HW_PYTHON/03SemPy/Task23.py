# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# o [2, 3, 4, 5, 6] => [12, 15, 16];
# o [2, 3, 5, 6] => [12, 15]

def SumOfPairs(list):
    result = []
    for i in range(len(list)//2):
        item = list[i]*list[(i + 1)*(-1)]
        result.append(item)
    if len(list) % 2:
        item = list[len(list)//2] ** 2
        result.append(item)
    return result
list1 = [2, 3, 4, 5, 6]
list2 = [2, 3, 5, 6]
print(SumOfPairs(list1))
print(SumOfPairs(list2))
