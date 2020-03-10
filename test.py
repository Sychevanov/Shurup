import random
bag = {'С уроном':[],
    'Без урона': {},
    'Метательное': [],
}

a = [{'нож': [2,2,90]}]
b = [{'нож2': [3,3,90]}]
bag['Метательное'].append([{'нож': [2,2,90]}])
bag['Метательное'].append(b)
bag = {'Оружие':[],
        'Предметы': {},
        'Метательное': [],
    }


items =            {'Старый меч': [1,4],
    'Старый кременевый питослет': [2,3],
                    'Старый лук': [0,6],}
snaryajenie = {'Голова': 0,
              'Куртка': 0,
               'Обувь': 0,
                'Руки': [],
             'Кольцо1': 0,
             'Кольцо2': 0,
            'Ожерелье': 0,}

snaryajenie['Руки'].append({'Старый меч':[1,4]})
snaryajenie['Руки'].append({'Старый кременевый питослет':[2,3]})
#rand_items = {'Старый меч':[1,4,55]}
def items_in_bag(rand_items,bag):
  if len(list(rand_items.values())[0]) == 3:
    bag['Метательное'].append(rand_items)
#print(len(list(rand_items.values())[0]))
#items_in_bag(rand_items,bag)
print(len(bag['Метательное']))
print(bag)