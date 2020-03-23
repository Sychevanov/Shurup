from arcanum_fx.items_mob import snaryajenie,bag

char = {'Здоровье': 100,
            'Сила': 1,
        'Ловкость': 1,
         'Обаяние': 1,
      'Технологии': 1,
           'Магия': 1,
                     }
def info_char(char,snaryajenie,name):
    print(f'Имя персонажа {name}')
    for key in char:
        print(key,' - ', char[key])
    #перебрать снарежние и вывести что есть чего нет, моеэт быть генераторами и  ввообще синхронно
    print('')
    for key in snaryajenie:
        if len(snaryajenie[key])==0:
            print(key,' Пусто')
        else:
            print(key,' - ', list(snaryajenie[key].keys())[0],' ',list(snaryajenie[key].values())[0][0],' - ',list(snaryajenie[key].values())[0][1] )
    input('\nДля того, чтобы верунться назад нажмите Enter: ')
def jornal(bag):
    pass
