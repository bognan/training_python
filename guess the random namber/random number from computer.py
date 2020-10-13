import random

number = random.randint(1, 100)

users_count = int(input('Введите количество игроков: '))
users_list = []
for i in range(users_count):
    user_name = (input(f'Введите имя игрока {i}: '))
    users_list.append(user_name)

count = 1
levels = {1: 10, 2: 5, 3: 3}

level = int(input('Выбирете уровень сложности: '))
max_count = levels[level]

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('Все игроки проиграли')
        break
    for user in users_list:
        print(f'Ход игрока {user}')
        user_number = int(input(f'{user} введите ваше число: ', ))
        if number == user_number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('Ваше число больше')
        else:
            print('Ваше число меньше')
else:
    print(f'Вы угадали число c {count} попыток. {winner_name} победил!')
