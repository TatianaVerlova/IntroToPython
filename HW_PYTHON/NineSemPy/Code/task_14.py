# 14). Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11


def sum_of_digits(number_str):
    number_str = str(number_str)
    lst = []
    for i in range(len(number_str)):
        if number_str[i].isdigit():
            lst.append(int(number_str[i]))
    my_sum = 0
    for i in range(len(lst)):
        my_sum += lst[i]
    return my_sum


num = input("Введите число для вычисления sum_of_digits: ")
print(sum_of_digits(num))
