# 18). Реализуйте алгоритм перемешивания списка.

from random import randint
lst = [1, 2, 3, 4, 5]
lst_mix = []
for i in range(len(lst)):
    index = randint(0, len(lst) - 1)
    lst_mix.append(lst[index])
    lst.pop(index)
print(lst_mix)