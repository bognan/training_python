first_name = str(input("Введите имя: ", ))
last_name = str(input("Введите фамилию: ", ))
patronymic = str(input("Введите отчество: ", ))
age = int(input("Введите ваш возраст: ", ))
weight = int(input("Введите ваш вес: ", ))

print("---------------->")

if (age < 30) and (50 >= weight < 120):
    print(last_name, first_name, patronymic)
    print("Возраст:", str(age) + ',', "вес:", weight)
    print("Пациент в хорошем состоянии.")
elif (30 <= age < 40) and (weight < 50 or weight > 120):
    print(last_name, first_name, patronymic)
    print("Возраст:", str(age) + ',', "вес:", weight)
    print("Пациенту требуется начать правильный образ жизни.")
elif (age >= 40) and (weight < 50 or weight > 120):
    print(last_name, first_name, patronymic)
    print("Возраст:", str(age) + ',', "вес:", weight)
    print("Пациенту требуется врачебный осмотр.")