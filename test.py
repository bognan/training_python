dict_month = {'01': 'января',
              '02': 'февраля',
              '03': 'марта',
              '04': 'апреля',
              '05': 'мая',
              '06': 'июня',
              '07': 'июля',
              '08': 'августа',
              '09': 'сентября',
              '10': 'октября',
              '11': 'ноября',
              '12': 'декабря',
              }

data = input('В ведите дату в формате дд.мм.гггг',)

day = data[0:2]
print(day)

month = data[3:5]
print(month)


print(dict_month[month])
#print(list(dict_month.keys()))

#print(dict_month['01'])