# 14). Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11


from unittest import TestCase


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


num = input("Введите число: ")
print(sum_of_digits(num))


class TestSumOfDigits(TestCase):

    def test_sum_of_digits_int(self):
        self.assertEqual(sum_of_digits(6782), 23)

    def test_sum_of_digits_float(self):
        self.assertEqual(sum_of_digits(0.56), 11)
