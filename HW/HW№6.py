my_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_list_2 = []

for number in my_list_1:
    if number not in my_list_2:
        my_list_2.append(number)
print(my_list_2)