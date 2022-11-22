# 16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.

num = int(input("Введите число: "))
result = []
if num > 0:
    for i in range(1, num + 1):
        result.append(round((1 + 1 / i) ** i, 2))
my_sum = 0
for i in range(len(result)):
    my_sum += result[i]
print(my_sum)

# Хочу еще раз попросить в каждой задаче писать пример ввода и вывода.
