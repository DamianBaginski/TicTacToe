def board():
    print('|' + position[0] + '|' + position[1] + '|' + position[2] + '|')
    print('-------')
    print('|' + position[3] + '|' + position[4] + '|' + position[5] + '|')
    print('-------')
    print('|' + position[6] + '|' + position[7] + '|' + position[8] + '|')
    print('-------')


def user_input(position_nr, if_taken):
    input_of_user = int(input('Wpisz pozycje: '))
    if input_of_user < 1 or input_of_user > 9:
        print('Nie ma takiej pozycji')
        raise SystemExit(0)
    if not if_taken[input_of_user - 1]:
        if stage % 2 == 1:
            position_nr[input_of_user - 1] = 'o'
        else:
            position_nr[input_of_user - 1] = 'x'
        if_taken[input_of_user - 1] = True
        return position_nr, if_taken
    else:
        print('Nie ma takiej mozliwosci')
        raise SystemExit(0)


def check_win(win, where_values_o, where_values_x):
    occupied_groups = 0
    for winning_combination in win:
        if any(element_of_combination in where_values_o for element_of_combination in winning_combination) and \
                any(element_of_combination in where_values_x for element_of_combination in winning_combination):
            occupied_groups = occupied_groups + 1
            if occupied_groups == 8:
                print('Remis!')
                board()
                raise SystemExit(0)
        if all(element_of_combination in where_values_o for element_of_combination in winning_combination) or \
                all(element_of_combination in where_values_x for element_of_combination in winning_combination):
            if stage % 2 == 0:
                print('x wins!')
            else:
                print('o wins!')
            board()
            raise SystemExit(0)


def index_ox(position_nr, indexes, indexes_2):
    for index in range(len(position_nr)):
        value = position_nr[index]
        if value == 'o':
            indexes.append(index)
        elif value == 'x':
            indexes_2.append(index)


pas_x = []
pas_o = []
position = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
stage = 0
winning_numbers = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
occupied = [False] * 9

while stage <= 9:
    stage += 1
    board()
    user_input(position, occupied)
    if stage > 4:
        index_ox(position, pas_o, pas_x)
        check_win(winning_numbers, pas_o, pas_x)
        pas_o.clear()
        pas_x.clear()
