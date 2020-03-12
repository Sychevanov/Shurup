import os
import random
from arcanum_fx.items_mob import *
from arcanum_fx.fight import *
def dungeon(conteiners,items2,s,n,m):  
    rand_cont = random.choice(conteiners)
    rand_enem = random.choice(list(enemy.keys())) #если что заменить list(enemy.keys()) на enemy str
    rand_items = random.choice(list(items.items()))
    rand_items2 = random.choice(list(items.items()))# в рвнд итем в йункцию добваления в сумку нужно передавать элемент словаря а передается тольок ключ
    while True:
        
        x = oglyadivaine(s)  
        os.system('cls' if os.name == 'nt' else 'clear')
        if x == 1:    
            if s[0][len(s[0])-11:] != '(Осмотрено)'  :            
                print(f'\nОсматривая {s[0]} Вы находите {rand_items[0]} и кладете к себе в сумку') #здесь может быть добавить взять предмет или не взять
                items_in_bag({rand_items[0]:rand_items[1]},bag) #не видит в бег осмотор новых вещей
                s[0] = s[0] + '(Осмотрено)'                 
            else:
                print('\nЗдесь уже ничего нет')       
        if x == 2:
            if s[1][len(s[1])-11:] != '(Осмотрено)'  :        
                print(f'\nВы начинаете битву против {s[1]}')
                if  fight(char,enemy,s[1],mana_virgil)!= True:
                    s[1] = s[1] + '(Осмотрено)'
            else:
                print('\nВы их уже убили')             
        if x == 3:
            if n == 0:
                return True
            if m:
                print('\nВы идете дальше по пещере и вновь сзади обрушивается проход, назад дороги нет')
            else:
                print(f'\nВы заходите, и сзади обрушивается проход, назад дороги нет')           
            p = [rand_cont,rand_enem,'Идти дальше','Осмотреться','Воспользоваться свитком вовращения']
            m = True
            return dungeon(conteiners,items,p,n-1,m)
        if x == 4:
            if s[3][len(s[3])-11:] != '(Осмотрено)'  :              
                print(f'\nВы видите {random.choice(conteiners)}. ')
                print(f'Шаря, вы нашли {rand_items2[0]} и взяли это себе')
                items_in_bag({rand_items2[0]:rand_items2[1]},bag)
                s[3] = s[3] + '(Осмотрено)'
            else:
                print('\nЗдесь уже ничего нет')        
        if x == len(s):
            if m:
                if len(bag) != 0:
        #       if len(bag['Предметы']) != 0:
                    for i in range(0,len(bag)):
        #           for i in range(0,len(bag['Предметы'])):
                        if i+1 == len(bag):
        #               if i == len(bag['Предметы']):
                           print('У вас нет Свитка возвращения')# протестировать свиток вовзарщения
                        if list(bag[i].keys())[0] == 'Свиток возвращения':
        #               if list(bag['Предметы'][i].keys())[0] == 'Свиток возвращения':
                           print(f'Вы использовали свиток возвращения и телепортируетесь. ')
                           return
                else:
                    print('Ваша сумка пуста')
            else:
                print('\nВы выходите', end = '')
                return
        if x == 6:
            bag_osmotr(bag)
            os.system('cls' if os.name == 'nt' else 'clear')
            

    
def oglyadivaine(s):
    print('\nВы решили оглядеться.')
    print(f'\nВаш взор падает на:')
    for i in range(len(s)):
        print(f'{i+1}. {s[i]}')
    print('------------------------')
    print('6. Сумка') #вот здесь и ниже сделтаь на проверку инт стр, тчобы не вводить 6, а ввовдить буклву B
    x = int(input('\nКуда вы решите подойти: '))
    print('\n\n\n\n\n\n\n||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||')
    return x