from unittest import TestCase, main
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
from HW_PYTHON.NineSemPy.Code.task_14 import sum_of_digits
from HW_PYTHON.NineSemPy.Code.task_15 import fact, NegativeNumber
from HW_PYTHON.NineSemPy.Code.task_16 import making_sequence, get_sum, NegativeNumber
from HW_PYTHON.NineSemPy.Code.task_23 import sum_of_pairs

class TestSumOfDigits(TestCase):

    def test_sum_of_digits_int(self):
        self.assertEqual(sum_of_digits(6782), 23)

    def test_sum_of_digits_float(self):
        self.assertEqual(sum_of_digits(0.56), 11)


class TestFactorial(TestCase):

    def test_factorial_positive(self):
        self.assertEqual(fact(4), [1, 2, 6, 24])

    def test_factorial_negative(self):
        self.assertRaises(NegativeNumber, fact, -4)


class TestSumOfSequence(TestCase):

    def test_making_sequence_positive(self):
        self.assertEqual(making_sequence(2), [2, 2.25])

    def test_making_sequence_negative(self):
        self.assertRaises(NegativeNumber, making_sequence, -2)

    def test_get_sum_of_lst(self):
        self.assertEqual(get_sum([2, 2.25]), 4.25)


class TestSumOfPairs(TestCase):

    def test_get_sum_of_pairs_odd(self): # нечетное кол-во эл-тов в списке
        self.assertEqual(sum_of_pairs([2, 3, 4, 5, 6]), [12, 15, 16])

    def test_get_sum_of_pairs_even(self): # четное кол-во эл-тов в списке
        self.assertEqual(sum_of_pairs([2, 3, 5, 6]), [12, 15])

    def test_get_sum_of_empty(self):
        self.assertEqual(sum_of_pairs([]), ([]))


if __name__ == '__main__':
    main()
