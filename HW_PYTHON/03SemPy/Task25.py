# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# o 45 -> 101101
# o 3 -> 11
# o 2 -> 10

def ScaleOfNotation(num): 
    if num < 2:
        return str(num)
    else:
        next = str(int( * round(num % 2, 1)))
        num = int(num // 2)
        return ScaleOfNotation(num) + next
number = int(input('Введите число: '))
print(ScaleOfNotation(number))