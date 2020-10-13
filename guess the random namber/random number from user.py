import random

number_comp = random.randint(1, 100)


win = False
num_list = []
count = 0

while not win:
    print(f'Вы загадали число: {number_comp}?')
    num_list.append(number_comp)
    answ_user = str(input())
    if answ_user == '=':
        win = True
        print(f'Компьютер победил')
    elif answ_user == '>':
        number_comp = random.randint(num_list[count], 100)
    elif answ_user == '<':
        number_comp = random.randint(1, num_list[count])
    count += 1
