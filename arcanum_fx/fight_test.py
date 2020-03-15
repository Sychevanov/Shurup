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