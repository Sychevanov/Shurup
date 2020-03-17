if x == 2:
                if len(bag['Метательное'])!=0:
                    for i in range(len(bag['Метательное'])): #сделать открыттие сумки, вернуть свою фуцнкцию,  и чтобы открывалсь вся сумка, можно выбрать все, но акетуально только метательное
                        a=''
                        a = list(bag['Метательное'][i].keys())[0]# вот здесь еслич то сиправить и нижке, потому что нао чтобы был массив словарей а не массив массивов внутри слоаврь
                        print(f'{i+1}. {a}: {bag["Метательное"][i][a][0]} - {bag["Метательное"][i][a][1]}')    
                    print('------------------------')
                    print('6. Назад')
                    bag_osmotr_met(bag)
                    x = int(input('Введите что вы хоитте метнуть: '))
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if x != 6:
                        od = od - 1
                        u = list(bag["Метательное"][x-1].keys())[0]   
                        atack = random.randint(bag["Метательное"][x-1][u][0],bag["Метательное"][x-1][u][1])
                        shanse_popad = bag["Метательное"][x-1][u][2]
                        print(f'\nВы Метнули во врага {u}' ) 
                        del bag['Метательное'][x-1] 
                        if miss(shanse_popad):  
                            health_enemy = health_enemy - atack 
                            print(f'\nВы нанесли урона: {full_hp - health_enemy}')
                            full_hp = health_enemy
                        else: 
                            print('\nВы промахнулись') 
                    elif x==6:
                        print('Вы передумали')

def items_in_bag2(rand_items,bag):
  if len(list(rand_items.values())[0]) == 3:
    bag['Метательное'].append(rand_items)
  if len(list(rand_items.values())[0]) == 2:
    bag['Оружие'].append(rand_items)
  if len(list(rand_items.values())[0]) == 1:
    bag['Предметы'].append(rand_items)
    
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