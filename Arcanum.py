import random
from arcanum_fx.picture_draw import mashin,zastavka,dirijable,virdgil
from arcanum_fx.vibor_char import human,elf,dwarf,gnome,hobbit,poluelf,poluorc,poluogre
from arcanum_fx.sozdanie_char import sozdanie_char,sozdaine_char2
from arcanum_fx.char import char
from arcanum_fx.items_mob import items,snaryajenie,conteiners,enemy_str,items2,enemy
from arcanum_fx.dialogs import dialog_virgil 
from arcanum_fx.values import mana_virgil
from arcanum_fx.fight import atack,fight,vibor_atack,miss
from arcanum_fx.dungeon import dungeon,vibor_oglayd,oglyadivaine
s = ['','','','']

zastavka()
print('1. Новая игра')
print('2. Загрузить игру')
print('3. Выход')
x = int(input('Введите число: '))
rand_cont = random.choice(conteiners)
rand_enem = random.choice(enemy_str)
rand_items2 = random.choice(items2)
if x == 1: 
    sozdaine_char2()
    dirijable()
    dialog_virgil(s)
    print('\nПосле разговора с Вирджилом, Вы решили осмотреться, первым делом подошли к мертвому гному и нашли у него паспорт на имя Престона Рэдклиффа, посчитав, что вам это нужно, забрали его себе')
    s = ['Мертвого человека','Волков','Пещеру','Осмотреться','Идти с Вирджилом']
    if dungeon(conteiners,items2,s,2,rand_cont,rand_enem,rand_items2):
        print('\nИ видите духа, парящим над бездыханным телом, подходя ближе, вы ощущаете себя дурно\nно из-за любопытсва, начинаете с ним диалог')
    print('\nПроходя мимо разрушенного дирижабля, на теле одного из пассажиров, мы замечаете поломанный фотоаппарат, решив, что этот странный механизм мертовому все равно не нужен, положили к себе в сумку.')
    


    
