# 15). Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

from unittest import TestCase
class NegativeNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


def fact(number):
    factorial = 1
    result = []
    for i in range(1, number + 1):
        factorial *= i
        result.append(factorial)
    return result


num = int(input("Введите число: "))
try:
    if num < 0:
        raise NegativeNumber("Нельзя вводить отрицательные числа!")
except NegativeNumber as err:
    print(err)
else:
    print(fact(num))

class TestFactorial(TestCase):

    def test_factorial_positive(self):
        self.assertEqual(fact(4), [1, 2, 6, 24])

    def test_factorial_negative(self):
        self.assertEqual(fact(-4), [])
