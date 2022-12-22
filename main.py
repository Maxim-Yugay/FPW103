play_zone = list(range(1,10))

def game_board(play_zone):
    print('-' * 13)
    for i in range(3):
        print('|', play_zone[0 + i * 3],'|', play_zone[1 + i * 3],'|', play_zone[2 + i * 3], '|')
        print('-' * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = int(input('Куда поставить ' + player_token + '? '))
        if 1 <= player_answer <= 9:
            if str(play_zone[player_answer - 1]) not in 'XO':
                play_zone[player_answer - 1] = player_token
                valid = True
            else:
                print('Поле уже занято. Выберите другое поле.')
        else:
            print('Ошибка ввода. Введите число от 1 до 9.')


def chek_winner (play_zone):
    winn_comb = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in winn_comb:
        if play_zone[i[0]] == play_zone[i[1]] == play_zone[i[2]]:
            return play_zone[i[0]]

    return False

def main(play_zone):
    count = 0
    win = False
    while not win:
        game_board(play_zone)
        if count % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        count += 1
        if count > 4:
            a = chek_winner(play_zone)
            if a:
                print(a, 'выйграл.')
                win = True
                break
        if count == 9:
            print('Ничья.')
            break


main(play_zone)


