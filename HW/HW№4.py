my_list_1 = [1, 1, 1, 2, 2, 2, 2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

for number in my_list_1[:]:
    if number in my_list_2:
        my_list_1.remove(number)

print(my_list_1)