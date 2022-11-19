# 2. Создайте программу для игры с конфетами человек против человека. Условие задачи: На столе лежит 2021 конфета. Играют два игрока 
# делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты 
# оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего 
# конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Игра между людьми:

# class Wrong_amount(Exception):
#     def __init__(self, txt):
#         self.txt = txt

# candies_amount = 2021
# permitted_extraction = 28
# player = randint(1, 2)
# while candies_amount >= 1:
#     if player == 1:
#         player = 2
#     else:
#         player = 1
#     extraction = int(input(f"Осталось {candies_amount} конфет. Игрок №{player}, какое количество конфет вы возьмете? "))
#     try:
#         if 0 < extraction > permitted_extraction:
#             raise Wrong_amount("Вы не можете взять такое количество конфет! Игра окончена")
#     except Wrong_amount as err:
#         print(err)
#     else:
#         candies_amount -= extraction
# print(f"Выиграл игрок №{player}!")

# Игра с ботом:

# from random import randint

# class Wrong_amount(Exception):
#     def __init__(self, txt):
#         self.txt = txt

# candies_amount = 2021
# permitted_extraction = 28
# player = randint(1, 2)
# while candies_amount >= 1:
    # if player == 1:
    #     player = 2
    # else:
    #     player = 1
#     if player == 1:
#         extraction = int(input(f"Осталось {candies_amount} конфет. Какое количество конфет вы возьмете? "))
#         try:
#             if 0 < extraction > permitted_extraction:
#                 raise Wrong_amount("Вы не можете взять такое количество конфет! Игра окончена")
#         except Wrong_amount as err:
#             print(err)
#         else:
#             candies_amount -= extraction
#     else:
#         candies_amount -= randint(1, 28)
# print(f"Выиграл игрок №{player}!")

# Игра с ботом + "интеллект":

from random import randint

class WrongAmount(Exception):
    def __init__(self, txt):
        self.txt = txt

candies_amount = 100
permitted_extraction = 28
player = randint(1, 2)
while candies_amount >= 1:
    if player == 1:
        player = 2
    else:
        player = 1
    if player == 1:
        extraction = int(input(f"Осталось {candies_amount} конфет. Какое количество конфет вы возьмете? "))
        try:
            if 0 < extraction > permitted_extraction:
                raise WrongAmount("Вы не можете взять такое количество конфет! Игра окончена")
        except WrongAmount as err:
            print(err)
        else: 
            candies_amount -= extraction
    else:
        if candies_amount > permitted_extraction:
            extraction = (candies_amount - permitted_extraction - 1) % permitted_extraction
            if extraction == 0: # игрок не может не взять конфету
                extraction = permitted_extraction
        else:
            extraction = candies_amount
        print(extraction)
        candies_amount -= extraction
print(f"Выиграл игрок №{player}!")