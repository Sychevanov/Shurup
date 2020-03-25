import random
from arcanum_fx.proverka import proverka 
items =            {'Старый меч': [1,4],
    'Старый кременевый пистолет': [2,3],
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
snaryajenie = {'Голова': {},
              'Куртка': {},
               'Обувь': {},
                'Руки': {},
             'Кольцо1': {},
             'Кольцо2': {},
            'Ожерелье': {},}
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



bag = []
      

def bag_osmotr(bag,snaryajenie):
  sortirovka(bag)
  print('--------------')
  print('-  Предметы  -')
  print('--------------\n')
  for i in range(0,len(bag)):
    if len(list(bag[i].values())[0]) == 1:
      print(i+1,'.',list(bag[i].keys())[0])
  print('\n--------------')
  print('-   Оружие   -')
  print('--------------\n')
  for i in range(0,len(bag)):
    if len(list(bag[i].values())[0]) == 2:
      print(i+1,'.',list(bag[i].keys())[0], list(bag[i].values())[0][0],'-', list(bag[i].values())[0][1])
  print('\n-------------')
  print('-Метательное-')
  print('-------------\n')
  for i in range(0,len(bag)):
    if len(list(bag[i].values())[0]) == 3:
      print(i+1,'.',list(bag[i].keys())[0], list(bag[i].values())[0][0],'-',list(bag[i].values())[0][1])
  print('--------------')
  print(f'\n{len(bag)+1}. Назад\n')
  x = proverka('Выберете предмет, который хотите взять в руки: ',1,len(bag)+1)
  return x
def type_predmet(item):
    if len(list(item.values())[0]) == 1:
      return 'Предмет'
    if len(list(item.values())[0]) == 2:
      return 'Оружие'
    if len(list(item.values())[0]) == 3:
      return 'Метательное'
      

def items_in_bag(rand_items,bag):
  bag.append(rand_items)

def sortirovka(bag):
  found=False
  while not found:
      found = True
      for i in range(len(bag)-1):
          if len(list(bag[i].values())[0])>len(list(bag[i+1].values())[0]):
            bag[i],bag[i+1] = bag[i+1],bag[i]
            found = False
