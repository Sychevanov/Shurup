import random
import os
from arcanum_fx.picture_draw import mashin,zastavka,dirijable,virdgil
from arcanum_fx.vibor_char import human,elf,dwarf,gnome,hobbit,poluelf,poluorc,poluogre
from arcanum_fx.sozdanie_char import sozdanie_char,sozdaine_char2
from arcanum_fx.char import char
from arcanum_fx.items_mob import *
from arcanum_fx.dialogs import dialog_virgil 
from arcanum_fx.values import mana_virgil
from arcanum_fx.fight import atack,fight,vibor_atack,miss
from arcanum_fx.dungeon import dungeon,oglyadivaine
from arcanum_fx.proverka import proverka
from arcanum_fx.arcanum_save import load
s = ['','','','',]
os.system('cls' if os.name == 'nt' else 'clear')
zastavka()
print('1. Новая игра')
print('2. Загрузить игру')
print('3. Выход')
x = proverka('Введите число: ',1,3)
os.system('cls' if os.name == 'nt' else 'clear')    
while True:
    if x == 3:
        break
    if x == 1: 
        name = sozdaine_char2()
        dirijable()
        dialog_virgil(s)
        rand_items = {'Старый меч':[1,4]}
        items_in_bag(rand_items,bag)
        rand_items = {'Свиток возвращения':[10]}
        items_in_bag(rand_items,bag)
        print('\nПосле разговора с Вирджилом, Вы решили осмотреться.\nПервым делом подошли к мертвому гному и нашли у него паспорт на имя Престона Рэдклиффа, посчитав, что вам это нужно, забрали его себе')
        rand_items = {'Метательный нож':[1,4,90]}
        items_in_bag(rand_items,bag)
        rand_items = {'Паспорт на имя Престона Редклифа':[10]}
        items_in_bag(rand_items,bag)
        input('\nНажмите любую клавишу для продолжения: ')
        os.system('cls' if os.name == 'nt' else 'clear')
        s = ['Мертвого человека','Волков','Пещеру','Осмотреться','Идти с Вирджилом']
    if x == 2: #нелогичная система загрузки, передлывать пока не буду 
        load = load()
        name = load[0]
        char = load[1]
        snaryajenie = load[2]  
        bag = load[3]
        s = load[4]
        print('Вы загрузили игру\n')  
        input('\nНажмите любую клавишу для продолжения: ')
        os.system('cls' if os.name == 'nt' else 'clear')
    
    final_dungeon = dungeon(conteiners,items2,s,2,False,name,char,snaryajenie,bag)
    if final_dungeon[0]:
        print('\n\nПроходя дальше вы видите духа, парящим над бездыханным телом. Подходя ближе, вы ощущаете себя дурно\nно из-за любопытсва, начинаете с ним диалог')
        #и событие
    elif final_dungeon[1]:
        print('Вы вышли из игры')
        break
    print('\n\nПроходя мимо разрушенного дирижабля, на теле одного из пассажиров, мы замечаете поломанный фотоаппарат, решив, что этот странный механизм мертовому все равно не нужен, положили к себе в сумку.')
    rand_items = {'Разбитый фотоаппарат':[20]}
    items_in_bag(rand_items,bag)
    print('Пре-альфа тест окончен')
    break
    


    


    
