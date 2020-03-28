import os
import random
from arcanum_fx.items_mob import items,enemy,conteiners,type_predmet,bag_osmotr,items_in_bag,sortirovka
from arcanum_fx.fight import *
from arcanum_fx.menu import menu
from arcanum_fx.char import info_char,jornal
from arcanum_fx.proverka import proverka
from arcanum_fx.arcanum_save import save,load
def dungeon(conteiners,items2,s,n,m,name,char,snaryajenie,bag):  
    final = [0,0] #0 - финал собитие 1 - выход из игры
    rand_cont = random.choice(conteiners)
    rand_enem = random.choice(list(enemy.keys())) 
    rand_items = random.choice(list(items.items()))
    rand_items2 = random.choice(list(items.items()))
    while True:
        x = oglyadivaine(s)  
        os.system('cls' if os.name == 'nt' else 'clear')
        if x == 1:    
            if s[0][len(s[0])-11:] != '(Осмотрено)'  :            
                print(f'\nОсматривая {s[0]} Вы находите {rand_items[0]} и кладете к себе в сумку') #здесь может быть добавить взять предмет или не взять
                items_in_bag({rand_items[0]:rand_items[1]},bag)
                s[0] = s[0] + '(Осмотрено)'                 
            else:
                print('\nЗдесь уже ничего нет')       
        if x == 2:
            if s[1][len(s[1])-11:] != '(Осмотрено)'  :        
                print(f'\nВы начинаете битву против {s[1]}')
                if  fight(char,enemy,s[1],mana_virgil,bag,snaryajenie)!= True:
                    s[1] = s[1] + '(Осмотрено)'
            else:
                print('\nВы их уже убили')             
        if x == 3:
            if n == 0:
                final[0] = 1
                return final
            if m:
                print('\nВы идете дальше по пещере и вновь сзади обрушивается проход, назад дороги нет')
            else:
                print(f'\nВы заходите, и сзади обрушивается проход, назад дороги нет')           
            p = [rand_cont,rand_enem,'Идти дальше','Осмотреться','Воспользоваться свитком вовращения']
            m = True
            return dungeon(conteiners,items,p,n-1,m,name,char,snaryajenie,bag)
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
                    for i in range(0,len(bag)):
                        if i+1 == len(bag):
                           print('У вас нет Свитка возвращения')
                        if list(bag[i].keys())[0] == 'Свиток возвращения':
                           print(f'Вы использовали свиток возвращения и телепортируетесь. ')
                           return final 
                else:
                    print('Ваша сумка пуста')
            else:
                print('\nВы выходите', end = '')
                return final
        if x == 6:
            while True:          
                x = bag_osmotr(bag,snaryajenie)   
                if x == len(bag)+1:
                    break
                if x>0 and x<len(bag)+1:
                    if type_predmet(bag[x-1]) != 'Оружие' :
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f'Думаете с {list(bag[x-1].keys())[0]} в руках вы нанесете врагу серьезный урон?\nСоветую взять оружие\n')
                        input('Enter для продолжения: ')
                    else: 
                        os.system('cls' if os.name == 'nt' else 'clear')
                        y = proverka(f'Хотите взять в руки {list(bag[x-1].keys())[0]}?\n\n1. Да  \n2. Нет\n',1,2)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        if y == 1:
                            print(f'Вы кладете в сумку {snaryajenie["Руки"]}\n')
                            items_in_bag(snaryajenie['Руки'],bag)
                            snaryajenie['Руки'] = bag[x-1] 
                            print(f'Вы взяли в руки {list(bag[x-1].keys())[0]}\n')                        
                            del bag[x-1]
                            input('Enter для продолжения: ')
                        else:
                            print('Вы передумали')
                os.system('cls' if os.name == 'nt' else 'clear')
            os.system('cls' if os.name == 'nt' else 'clear')
            x = 0
        if x == 7:
            info_char(char,snaryajenie,name)
            os.system('cls' if os.name == 'nt' else 'clear')
        if x == 8:
            jornal(bag)
            os.system('cls' if os.name == 'nt' else 'clear')
        if x == 9:
            y = menu()
            if y == 1:
                if m:
                    print('Сохраниться в пещере нельзя')
                    input('Enter для продолжения: ')
                else:
                    save(name,char,snaryajenie,bag,s)
                    print('Ваша игра сохранена\n')
                    input('Enter для продолжения: ')
            if y == 3:
                final[1] = 1
                return final
            os.system('cls' if os.name == 'nt' else 'clear')
        

    
def oglyadivaine(s):
    print('\nВы решили оглядеться.')
    print(f'\nВаш взор падает на:')
    for i in range(len(s)):
        print(f'{i+1}. {s[i]}')
    print('------------------------')
    print('6. Сумка')
    print('7. О персонаже')
    print('8. Журнал(В разработке) ')
    print('------------------------')
    print('9. Меню')
    x = proverka('\nКуда вы решите подойти: ',1,9)
    print('\n\n\n\n\n\n\n||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||')
    return x