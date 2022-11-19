# 3. Создайте программу для игры в ""Крестики-нолики"".
from random import randint

player = randint(1, 2)    

field = \
    {
        'a_1': 'a_1',
        'a_2': 'a_2',
        'a_3': 'a_3',
        'b_1': 'b_1',
        'b_2': 'b_2',
        'b_3': 'b_3',
        'c_1': 'c_1',
        'c_2': 'c_2',
        'c_3': 'c_3'
    }

for i in range(0,9):
    if field['a_1'] == field['a_2'] == field['a_3'] or\
        field['b_1'] == field['b_2'] == field['b_3'] or\
        field['c_1'] == field['c_2'] == field['c_3'] or\
        field['a_1'] == field['b_1'] == field['c_1'] or\
        field['a_2'] == field['b_2'] == field['c_2'] or\
        field['a_3'] == field['b_3'] == field['c_3'] or\
        field['a_1'] == field['b_2'] == field['c_3'] or\
        field['c_1'] == field['b_2'] == field['a_3']:
        print(f'Игрок {player} победил!')
        break
    else:
        if player == 1:
            player = 2
        else:
            player = 1
        print(f"{field['a_1']}   |   {field['a_2']}   |   {field['a_3']}\n_______________________\n{field['b_1']}   |   {field['b_2']}   |   {field['b_3']}\n_______________________\n{field['c_1']}   |   {field['c_2']}   |   {field['c_3']}")
        new_move = input(f"Игрок {player}, ваш ход (введите позицию, например 'a_1'): ")
        if player == 1:
            field[new_move] = ' x '
        else:
            field[new_move] = ' o '
else:
    print('Ничья!')