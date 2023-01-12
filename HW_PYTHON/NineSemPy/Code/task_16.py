# 16). Задайте список из n чисел последовательности 〖(1+1/n)〗^n и выведите на экран их сумму.


class NegativeNumber(Exception):
    def __init__(self, txt):
        self.txt = txt


def making_sequence(number):
    try:
        if number < 0:
            raise NegativeNumber("Нельзя вводить отрицательные числа!")
    except NegativeNumber as err:
        print(err)
    else:
        result = []
        for i in range(1, number + 1):
            result.append(round((1 + 1 / i) ** i, 2))
        return result

def get_sum(lst):
    lst_sum = 0
    for i in range(len(lst)):
        lst_sum += lst[i]
    return lst_sum


num = int(input("Введите число для вычисления making_sequence: "))
sequence = making_sequence(num)
print(get_sum(sequence))
