# 17). Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные) хранятся в 
# файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.

# Пример:
# Файл:
# 4
# 5
# 2
# N = 3 => [-3, -2, -1, 0, 1, 2, 3]
# Результат: 1*2*(-1) = -2

num = int(input("Введите число: "))
list = []
for i in range(-num, num + 1):
    list.append(i)
i = 0
elements = []
for i in range(0, len(list), 2):
    elements.append(i)
with open('Task17.txt', 'w') as file:
    for element in elements:
        file.write(str(element) + '\n')
with open('Task17.txt', 'r') as file:
    elements_1 = file.read().splitlines()
result = 1
for i in range(len(list)):
    for j in range(len(elements_1)):
        if i == int(elements_1[j]):
            result *= list[i]
print(result)