# 18). Реализуйте алгоритм перемешивания списка.

import random
from random import randint
list = [1, 2, 3, 4, 5]
list_mix = []
for i in range(len(list)):
    index = randint(0, len(list) - 1)
    list_mix.append(list[index])
    list.pop(index)
print(list_mix)