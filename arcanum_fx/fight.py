import random
import os
import time
from arcanum_fx.values import mana_virgil
from arcanum_fx.items_mob import *
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
def miss(shance):
    if random.randint(0,100)<shance:
        return True
def atack(snaryajenie,char): # вот эта функция не работает
    return random.randint(snaryajenie['Руки'][0][0],snaryajenie['Руки'][0][1])+char['Сила']+char['Ловкость']
def fight(char,enemy,s,mana_virgil):
    if miss(50):
        od = 1
    else:
        od = 0
    atack_enemy = enemy[s][1]
    health_enemy = enemy[s][0]
    health_char = char['Здоровье']
    full_hp = enemy[s][0]
    i=0
    while True:
        x = 0
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
            print(f'                                                 Ваш ход ')
            print('------------------------------------------------------------------------------------------------------') 
            if x == 1:
                od = od - 1
                print('\nВы атакуете')  
                atack = random.randint(list(snaryajenie['Руки'][0].values())[0][0],list(snaryajenie['Руки'][0].values())[0][1])+char['Сила']+char['Ловкость']
                if miss(50):  
                    health_enemy = health_enemy - atack
                    #health_enemy = health_enemy - atack(snaryajenie,char) вот здесь почему-о не работает функция атаки
                    print(f'\nВы нанесли урона: {full_hp - health_enemy}')
                    full_hp = health_enemy
                else: 
                    print('\nВы промахнулись') 
                
            if x == 2:
                if len(bag) != 0:                 
                    x = bag_osmotr_met(bag)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if len(list(bag[x-1].values())[0]) != 3:  
                        print(f'Вы можете метнуть {list(bag[x-1].keys())[0]}, но в этом не будет никакого смысла, только если разозлить')  
                        # и сюда добавить хотите ли вы метнуть?    
                    if len(list(bag[x-1].values())[0]) == 3:          
                        od = od - 1
                        shanse_popad = list(bag[x-1].values())[0][2]
                        atack = random.randint(list(bag[x-1].values())[0][0],list(bag[x-1].values())[0][1])
                        if miss(shanse_popad):  
                            health_enemy = health_enemy - atack 
                            print(f'\nВы метнули {list(bag[x-1].keys())[0]} и нанесли урона: {full_hp - health_enemy}')
                            full_hp = health_enemy
                            del bag[x-1]
                        else: 
                            print('\nВы промахнулись') 
                    x = 0
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
                if miss(50):
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
    