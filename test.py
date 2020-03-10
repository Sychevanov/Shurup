import random
items =            {'Старый меч': [1,4],
    'Старый кременевый питослет': [2,3],
                    'Старый лук': [0,6],
                    'Хлам':[5],
                    'Части пистолета':[7],
                    'Уголь':[3],
                    'Тряпку':[2],
                    'Проволку':[2],
                    'Механизм':[9],
                    'Ложку':[1],
                    'Тарелку':[1],
                    'Зелье здоровья':[15],
                    'Припарку':[15],
                    }
b = {}
rand_items = random.choice(list(items.items()))
print(rand_items )
a={rand_items[0]:rand_items[1]}
b[rand_items[0]]=rand_items[1]
print(a,b)

bag = {'Оружие':[],
        'Предметы': [],
        'Метательное': [],
    }

def items_in_bag(rand_items,bag):
  if len(list(rand_items.values())[0]) == 3:
    bag['Метательное'].append(rand_items)
  if len(list(rand_items.values())[0]) == 2:
    bag['Оружие'].append(rand_items)
  if len(list(rand_items.values())[0]) == 1:
    bag['Предметы'].append(rand_items)
    print()

def bag_osmotr(bag):
  for key in bag:
    if key == 'Предметы':
      if len(bag['Предметы']) != 0:
        for key2 in bag['Предметы'][0]:
            print(f'\n{key2}')
    if key == 'Оружие':
      if len(bag['Оружие']) != 0:
        for key3,val in bag['Оружие'][0].items():
            print(f'\n{key3}  {val}') #доделать что в руках, а что в сумке
    if key == 'Метательное':
      if len(bag['Метательное']) != 0:
        for key4,val2 in bag['Метательное'][0].items():
            print(f'\n{key4}  {val2}')
  return input('\nДля выхода нажмите любую кнопку: ')

items_in_bag({rand_items[0]:rand_items[1]},bag)
bag_osmotr(bag)

print(bag)