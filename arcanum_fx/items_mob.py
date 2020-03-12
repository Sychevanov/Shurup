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
snaryajenie = {'Голова': 0,
              'Куртка': 0,
               'Обувь': 0,
                'Руки': [],
             'Кольцо1': 0,
             'Кольцо2': 0,
            'Ожерелье': 0,}
conteiners = ["Ящик","Бочка(у)","Деревянный Сундук","Комод","Тумба(у)","Ведро","Контрейнер","Шкаф"]
#enemy_str = ['Крыс','Волков','Гоблинов','Медведей','Гарпий','Слизня','Чупокабру']
items2 = ['','','','','','','','','','']



enemy = {'Крыс': [10,2],
       'Волков': [15,3],
     'Гоблинов': [12,3],
     'Медведей': [20,3],
       'Гарпий': [10,5],
       'Слизня': [4,4],
       }

bag2 = {
        'Предметы': [],
        'Оружие':[],
        'Метательное': [],
    }

bag = []

def bag_osmotr2(bag):
  for key in bag:
    if key == 'Предметы':
      if len(bag['Предметы']) != 0:
        print('--------------')
        print('-  Предметы  -')
        print('--------------\n')
        for i in range(0,len(bag['Предметы'])):
          print(i+1,'.',list(bag['Предметы'][i].keys())[0])
    if key == 'Оружие':
      if len(bag['Оружие']) != 0:
        print('\n--------------')
        print('-   Оружие   -')
        print('--------------\n')
        for j in range(0,len(bag['Оружие'])):
          print(j+1+len(bag['Предметы']),'.',list(bag['Оружие'][j].keys())[0], list(bag['Оружие'][j].values())[0][0],'-', list(bag['Оружие'][j].values())[0][1])
    if key == 'Метательное':
      if len(bag['Метательное']) != 0:
        print('\n-------------')
        print('-Метательное-')
        print('-------------\n')
        for k in range(0,len(bag['Метательное'])):
          print(k+1+len(bag['Предметы'])+len(bag['Оружие']),'.',list(bag['Метательное'][k].keys())[0], list(bag['Метательное'][k].values())[0][0],'-',list(bag['Метательное'][k].values())[0][1])
  return input('\nДля выхода нажмите любую кнопку: ')       

def bag_osmotr(bag):
  for i in range(0,len(bag)):
    if len(list(bag[i].values())[0]) == 1:
      print(i+1,'.',list(bag[i].keys())[0])
    if len(list(bag[i].values())[0]) == 2:
      print(i+1,'.',list(bag[i].keys())[0], list(bag[i].values())[0][0],'-', list(bag[i].values())[0][1])
    if len(list(bag[i].values())[0]) == 3:
      print(i+1,'.',list(bag[i].keys())[0], list(bag[i].values())[0][0],'-',list(bag[i].values())[0][1])
  return input('\nДля выхода нажмите любую кнопку: ') 
  
def items_in_bag2(rand_items,bag):
  if len(list(rand_items.values())[0]) == 3:
    bag['Метательное'].append(rand_items)
  if len(list(rand_items.values())[0]) == 2:
    bag['Оружие'].append(rand_items)
  if len(list(rand_items.values())[0]) == 1:
    bag['Предметы'].append(rand_items)

def items_in_bag(rand_items,bag):
  bag.append(rand_items)