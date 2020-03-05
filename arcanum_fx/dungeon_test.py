import random
from arcanum_fx.items_mob import *
from arcanum_fx.fight import *
def dungeon(conteiners,items2,s,n,m):  
    rand_cont = random.choice(conteiners)
    rand_enem = random.choice(list(enemy.keys())) #если что заменить list(enemy.keys()) на enemy str
    rand_items2 = random.choice(items2)
    while True:
        if n == 0:
            return True
        x = oglyadivaine(s) 
        vibor_oglayd(x,s,conteiners,items2)         
        if x == 3:
            if m:
                print('\nВы идете дальше по пещере и вновь сзади обрушивается проход, назад дороги нет')
            else:
                print(f'\nВы заходите и сзади обрушивается проход, назад дороги нет')           
            p = [rand_cont,rand_enem,'Идти дальше','Осмотреться','Воспользоваться свитком вовращения']
            m = True
            return dungeon(conteiners,items2,p,n-1,m)
        if x == len(s):
            print('\nВы выходите', end = '')
            return
            #здесь поставтьи иф, если есть свиток вовзарщения тошгда ретерн, иначе не ретерн
        #вот здесь добавить иф с сумкой, если да то вызов сумки
def vibor_oglayd(x,s,conteiners,items2):
    if x == 1:    
        if s[0][len(s[0])-11:] != '(Осмотрено)'  :            
            print(f'\nОсматривая {s[0]} Вы находите {random.choice(items2)} ')
            s[0] = s[0] + '(Осмотрено)' 
            
        else:
            print('\nЗдесь уже ничего нет')
    if x == 4:
        if s[3][len(s[3])-11:] != '(Осмотрено)'  :              
            print(f'\nВы видите {random.choice(conteiners)}. ')
            print(f'Шаря, вы нашли {random.choice(items2)} и взяли это себе')
            s[3] = s[3] + '(Осмотрено)'
        else:
            print('\nЗдесь уже ничего нет')
    if x == 2:
        if s[1][len(s[1])-11:] != '(Осмотрено)'  :        
            print(f'\nВы начинаете битву против {s[1]}')
            if  fight(char,atack,enemy,s[1],mana_virgil)!= True:
                s[1] = s[1] + '(Осмотрено)'
        else:
            print('\nВы их уже убили')
def oglyadivaine(s):
    print('\nВы решили оглядеться.')
    print(f'\nВаш взор падает на:')
    for i in range(len(s)):
        print(f'{i+1}. {s[i]}')
    # вот сюда добавить сумку
    x = int(input('\nКуда вы решите подойти: '))
    print('\n\n\n\n\n\n\n||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||')
    return x