from itertools import count
from functools import reduce # позволяет применить любую функцию к массиву и свести всё к одному значению

# Лямбда-функции
#Есть массив л-тов, нужно вывести только те эл-ты массива, которые больше предыдущего.

lst = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst = [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i - 1]]
print(lst)

# Даны числа в пределах 20-240, наобходимо найти числа, кратный 20 и 21.

lst = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(lst)

# Нужно из массива взять элементы, которые не имеют повторений

lst = [300, 300, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst = [el for el in lst if lst.count(el) == 1]
print(lst)

# Генератор
# 4! = 1 * 2 * 3 * 4 - 4 факториал

def fact(n):
    factorial = 1
    for x in count(1): # не в пределах ДО чего, а в пределах ОТ чего. count импортируется: from itertools import count
        if x > n:
            break
        factorial = factorial * x
        yield factorial

n = int(input("Введите целое число: "))
i = 0
for el in fact(n):
    i += 1
    print(f"!{i} = {el}")

# Задача на функцию reduce
# Перемножить все элементы списка: [2, 3, 4, 5] = 2*3*4*5 = 120

lst = [x for x in range(100, 1001, 2)]
res = reduce(lambda item, item2: item * item2, lst)
print(res)