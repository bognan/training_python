import random
start_number = 1
end_number = 100
number_comp = random.randint(start_number, end_number)


win = False
count = 0

while not win:
    print(f'Вы загадали число: {number_comp}?')
    answ_user = str(input())
    if answ_user == '=':
        win = True
        print(f'Компьютер угадал c {count} попытки')
    elif answ_user == '>':
        start_number = number_comp + 1
        number_comp = random.randint(start_number, end_number)
    elif answ_user == '<':
        end_number = number_comp - 1
        number_comp = random.randint(start_number, end_number)
    count += 1
