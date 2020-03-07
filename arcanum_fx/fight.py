import random
import os
import time
from arcanum_fx.values import mana_virgil
from arcanum_fx.items_mob import snaryajenie
from arcanum_fx.char import char
from arcanum_fx.items_mob import bag_osmotr,bag
def vibor_atack(od,char,health_char,full_hp):
    print(f'\nУ вас {od} ОД, что вы будете делать?')
    print('\n||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||=||')    
    print(f'\n1. Атаковать                         **************************************************')
    print(f'2. Метнуть...                        **     Мана Вирджила: {mana_virgil}, Здоровье: {health_char}         **')
    print(f'3. Попытаться договориться             **************************************************')
    print(f'4. Попросить Вирджила вас вылечить   **            Здоровье врага: {full_hp}                **')
    print(f'5. Сбежать                           **************************************************') 
    x = int(input('Введите число: '))   
    os.system('cls' if os.name == 'nt' else 'clear')
    return x
def miss():
    if random.randint(0,100)<50:
        return True
def atack(snaryajenie,char):
    return random.randint(snaryajenie['Руки'][0],snaryajenie['Руки'][1])+char['Сила']+char['Ловкость']
def fight(char,atack,enemy,s,mana_virgil):
    if miss():
        od = 1
    else:
        od = 0
    atack_enemy = enemy[s][1]
    health_enemy = enemy[s][0]
    health_char = char['Здоровье']
    full_hp = enemy[s][0]
    i=0
    while True:
        i=i+1
        if health_enemy < 1:
            print('----------------------------------------------------------------------------------------------------')
            print('                                                 Вы победили')
            print('----------------------------------------------------------------------------------------------------')
            break
        if health_char<1:
            print('\nВас убили!')
            return True
        if od > 0:           
            x = vibor_atack(od,char,health_char,full_hp) 
            print('----------------------------------------------------------------------------------------------------')
            print(f'                                                 Ваш ход {i-1}')
            print('------------------------------------------------------------------------------------------------------') 
            if x == 1:
                od = od - 1
                print('\nВы атакуете')  
                if miss():  
                    health_enemy = health_enemy - atack(snaryajenie,char) 
                    print(f'\nВы нанесли урона: {full_hp - health_enemy}')
                    full_hp = health_enemy
                else: 
                    print('\nВы промахнулись') 
                
            if x == 2:
                if len(bag['Метательное'])!=0:
                    for i in range(len(bag['Метательное'])):
                        a=''
                        a = list(bag['Метательное'][i][0].keys())[0]# вот здесь еслич то сиправить
                        print(f'{i+1}. {a}: {bag["Метательное"][i][0][a][0]} - {bag["Метательное"][i][0][a][1]}')
                    x = int(input('Введите что вы хоитте метнуть: '))
                    u = list(bag["Метательное"][x-1][0].keys())[0]   
                    atack = random.randint(bag["Метательное"][x-1][0][u][0],bag["Метательное"][x-1][0][u][1])
                    od = od - 1
                    print(f'\nВы Метнули во врага {u}' )  
                    if miss():  
                        health_enemy = health_enemy - atack 
                        print(f'\nВы нанесли урона: {full_hp - health_enemy}')
                        full_hp = health_enemy
                    else: 
                        print('\nВы промахнулись') 
                else:
                    print('\nУ вас нет ничего для того, чтобы метнуть во врага')
            if x == 3:
                print('\nДоговориться не получилось')
            if x == 4:
                if mana_virgil < 21:
                    print('\nУ вирджила закончиась мана, он не сможет вас вылечить')
                else:
                    od = od -1
                    char["Здоровье"] = char["Здоровье"] + 20
                    mana_virgil = mana_virgil - 20
                    print('\nВирджил произносит заклинание на непонятном вам языке, и вы чувствуете себя легче')                
            if x == 5:
                od = od -1
                print('\nВы пытаетесь убежать от врага') 
                if miss():
                    print('Вы успешно убежали')
                    return True
                    break
                else:
                    print('Сбежать не удалось')
        elif od == 0:
            print('----------------------------------------------------------------------------------------------------')
            print(f'                                                 Ход Врага {i-1}')
            print('----------------------------------------------------------------------------------------------------')
            print('\nВраг атакует')
            health_char = health_char - atack_enemy
            print(f'\nВам нанесли {char["Здоровье"]-health_char} урона')
            char["Здоровье"] = health_char
            od = 1
    