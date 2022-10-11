# 19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

n = 10
a = 8
c = 9
m = 100
list = [7]
for i in range (1, n+1):
    list.append((a*list[i-1] + c) % m)
print(list)

# Решение с использованием модуля time:

# import time


# def Random_Set(start = 0,end = 1):
# seconds = time.time()
# Next = True
# while Next:
# Rand = end * (seconds % 1)
# if Rand >= start or Rand > end: Next = False


# return int(Rand)

# print(Random_Set(1,1000))