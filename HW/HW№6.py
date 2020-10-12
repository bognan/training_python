my_list_1 = [2, 2, 5, 12, 8, 2, 12]
my_list_2 = []

for number in my_list_1:
    if my_list_1.count(number) == 1:
        my_list_2.append(number)
    else:
        continue
print(my_list_2)