number = int(input('Введите любое число: ',))
while (number > 10) or (number < 0):
    number = int(input('Побробуйте еще: ',))
else:
    if number <= 10:
        print('Результат:', number ** 2)