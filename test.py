from arcanum_fx.items_mob import snaryajenie,bag
char = {'Здоровье': {'qkll':[0,1]},
            'Сила': 1,
        'Ловкость': 1,
         'Обаяние': 1,
      'Технологии': 1,
           'Магия': 1,
                     }

print(list(char['Здоровье'].keys())[0])


char['Здоровье'] = {'dddd':[0.2]}
char['Здоровье']['fff']=5
print(char)
