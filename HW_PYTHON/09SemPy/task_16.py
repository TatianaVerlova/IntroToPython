# 16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.
from unittest import TestCase


class NegativeNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


def making_sequence(number):
    result = []
    for i in range(1, number + 1):
        result.append(round((1 + 1 / i) ** i, 2))
    return result

def get_sum(lst):
    lst_sum = 0
    for i in range(len(lst)):
        lst_sum += lst[i]
    return lst_sum


num = int(input("Введите число: "))

try:
    if num < 0:
        raise NegativeNumber("Нельзя вводить отрицательные числа!")
except NegativeNumber as err:
    print(err)
else:
    sequence = making_sequence(num)

print(get_sum(sequence))

class TestSumOfSequence(TestCase):

    def test_making_sequence_positive(self):
        self.assertEqual(making_sequence(2), [2, 2.25])

    def test_making_sequence_negative(self):
        self.assertEqual(making_sequence(-2), [])

    def test_get_sum_of_lst(self):
        self.assertEqual(get_sum([2, 2.25]), 4.25)
