# 31). Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 70 = 2*5*7 => [2, 5, 7]
# 140 = 2*2*5*7 => [2, 2, 5, 7]
# 140|2
# 70|2
# 35|5
# 7|7

num = int(input('Введите число: '))
result = []
for i in range(2, num + 1): # строки 11-19 проверяют является ли делимое простым числом
    if num != 1:
        j = 2
        k = 0
        while j**2 <= i and k != 1:
            if i % j == 0:
                k = 1
            j += 1
        if k != 1:
            while num % i == 0:
                result.append(i)
                num = num / i 
print(result)