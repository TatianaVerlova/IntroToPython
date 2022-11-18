# 3. Создайте программу для игры в ""Крестики-нолики"".

def move(player):
    print(f"{field['a_1']}   |   {field['a_2']}   |   {field['a_3']}\n_________________\n{field['b_1']}   |   {field['b_2']}   |   {field['b_3']}\n_________________\n{field['c_1']}   |   {field['c_2']}   |   {field['c_3']}")
    new_move = input(f"Игрок {player}, ваш ход: ")
    field[new_move] = player

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

print(f"{field['a_1']}   |   {field['a_2']}   |   {field['a_3']}\n_________________\n{field['b_1']}   |   {field['b_2']}   |   {field['b_3']}\n_________________\n{field['c_1']}   |   {field['c_2']}   |   {field['c_3']}")

end_game = 0