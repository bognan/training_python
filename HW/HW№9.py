player = {'name': input('Введите имя персонажа: '), 'health': 100, 'damage': 30}
enemy = {'name': 'Goblin', 'health': 100, 'damage': 10}


def attack(person1, person2):
    person2['health'] = person2['health'] - person1['damage']


attack(enemy, player)
print(player)
attack(player, enemy)
print(enemy)
