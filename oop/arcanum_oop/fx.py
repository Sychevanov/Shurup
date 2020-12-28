def infoChar_menu():
    from menu import Menu
    from simpleMenuIItem import Simple_menu_item
    from menuItem import Menu_item
    from fx import foo, beginLocation1, textLocation1,infoChar_menu
    from newGame import newGame
    from picture_draw import zastavka, dirijable, virdgil, mashin
    from ArcanumMainMenu import ArcanumMainMenu
    from charRegystry import CharRegystry
    from item import Item

    infoChar_menu = Menu('О персонаже',flag = False)    
    infoChar_menu.addItems('Харакатеристики',CharRegystry().infoChar)
    infoChar_menu.addItems('Журнал',foo)
    infoChar_menu.addItems('Сумка',CharRegystry().bagToHands)
    return infoChar_menu

textLocation2 = '\nПосле крушения, Вы, как в первый раз наслаждаетесь, приятно пахнущими цветами, но откуда ни возьмись на вас напали.  \n'
def printStep():
   
    print('----------------------------------------------------------------------------------------------------')
    print('                                                 Ваш ход ')
    print('------------------------------------------------------------------------------------------------------')

def proverka(s,n1,n2):
    while True:
        x = input(s)
        try:
            x = int(x)
            if x >= n1 and x <= n2:
                break
            else: 
                print(f'Введите число от {n1} до {n2}')
        except:
            print('Введите цифру, а не букву')    
    return x

def foo():
    print('\nВ разработке')

def printChar():
        print('------------------')
        print('Выберите расу')
        print('------------------')


def human():
    print('Люди (Human): как обычно, полная усредненность, никаких бонусов и пенальти, никакой предрасположенности к магии или технологии. Достаточно неплохо ладят со всеми остальными расами.')
    print('Обычно люди — хороший выбор для новичков, или, возможно, Из человека к концу игры можно слепить специалиста, причём в любой области. ')

def elf():
    print('Эльфы (Elves): +1 Ловкость, +1 Обаяние, +1 склонность к магии. -10 Здоровье, -1 Сила')
    print('Прирожденные маги с аллергией на технологию. Эльфы достаточно высокомерно ведут себя со всеми остальными расами, а дварфов просто презирают.')
def dwarf():
    print('Карлики (Dwarves): +1 Сила, +10 здоровье, +1 склонность к технологии,-1 Обаяние, -1 Ловкость')
    print('Еще у дварфов плохо дело со скиллом Метание— наверное, руки коротки. Они с уважением относятся к людям и гномам, но недолюбливают эльфов.')
    print('Дварфы — прирожденные техники. Если собираетесь развивать персонажа-технолога, они — ваш выбор.')
def gnome():
    print('Гномы (Gnomes):  +2 ранга обаяние, -20 Здоровье.')
    print('Гномы — прекрасные торговцы, которых не интересует соперничество между магией и технологией.')
def hobbit():
    print('Хоббиты (Halflings): +2 Ловкость')
    print('Хоббиты любимы всеми расами, хотя и слывут лентяями. Если же мохноногий лежебока все-таки покинет свою нору, то ему самой природой суждено стать отличным вором.')
def poluelf():
    print('Полуэльфы (Half-Elves): +1 Ловкость, +1 Обаяние, +1 склонность к магии. -1 Здоровье , -1 ранг в каждом технологическом умении.')
    print('Полуэльфы унаследовали от своих эльфийских предков склонность к магии, к технологии они не очень предрасположены. Кроме того, они прекрасно ладят со всеми расами.')
def poluorc():
    print('Half-Orcs): +3 Сила (Strength), +20 Здоровье 2, -2 Внешность, -2 Обаяние.')
    print('Не слишком привлекательные внешне и обладающие взрывным темпераментом, полуорки — хорошие бойцы. Не такие сильные, как полуогры, но зато и не такие тупые.')
def poluogre():
    print(' Полуогры (Half-Ogres): +4 Сила , +1 броня, -1 Внешность , -4 Интеллект, ') 
    print(' Вот живая иллюстрация поговорки «сила есть, ума не надо». Гора мышц и самый минимум мозгов. Впрочем, играть за такого персонажа очень забавно.')
    print(' Просто почитайте фразы, которые выдает ваш подопечный, — хорошее настроение гарантировано. Однако, если не хотите пропустить некоторые квесты, поднимите своему персонажу интеллект.')

raceName = {'Человек': [human,[0,1,1,1,1,1,]],
            'Эльф': [elf,[-10,0,2,2,-1,2,]],
            'Карлик': [dwarf,[+10,2,0,0,2,-1,]],
            'Гном': [gnome,[-20,0,0,+2,0,0,]],
            'Хоббит': [hobbit,[0,0,+2,0,0,0,]],
            'Полуэльф': [poluelf,[0,0,2,+1,0,0,]],
            'ПолуОрк': [poluorc,[+20,+4,0,-1,0,0,]],
            'Полуогр': [poluogre,[+30,+5,0,0,0,0,]],
                                     
                                }

def beginLocation1():
    print('\nПосле разговора с Вирджилом, Вы решили осмотреться.\nПервым делом подошли к мертвому гному и нашли у него паспорт на имя Престона Рэдклиффа, посчитав, что вам это нужно, забрали его себе\nНемного придя в себя, вы решили оглядеться.\n ')
def textLocation1():
    print('Пробираясь мимо разбросанных деталей дирижабля и кучи трупов, в скале вы видите пещеру.\n')




    