import os
#from arcanum_fx.vibor_char import human,elf,dwarf,gnome,hobbit,poluelf,poluorc,poluogre
#from arcanum_fx.char import char
#from arcanum_fx.items_mob import items, snaryajenie
#from arcanum_fx.proverka import proverka


from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo
from picture_draw import zastavka
def create():
    def sozdanie_char():
        print('------------------')
        print('Выберите расу')
        print('------------------')
        #print('1.Человек')
        #print('2.Эльф')
        #print('3.Карлик')
        #print('4.Гном')
        #print('5.Хоббит')
        #print('6.Полуэльф')
        #print('7.Полуорк')
        #print('8.Полуогр')
        #print('------------------')
    def test():
        print('Для продолжения нажмите назад')
    main_menu = Menu(title='',flag=True,noBack=False)
    main_menu.setStartupCommand(sozdanie_char)
    human = main_menu.addSubMenu('Человек2',True)
    human.addItems('1',foo)

    main_menu.addItems('Человек', foo)
    main_menu.addItems('Орк', foo)
    human.setNoExitCommand()


    main_menu.run()
    





def sozdaine_char2():
    while True:  
        sozdanie_char()
        x = proverka('Введите расу. Для подробного описания, введите цифру дважды: ',1,88)
        os.system('cls' if os.name == 'nt' else 'clear')
        if x == 11:
            human() 
        if x == 22:
            elf() 
        if x == 33:
            dwarf()
        if x == 44:
            gnome()
        if x == 55:
            hobbit()
        if x == 66:
            poluelf()
        if x == 77:
            poluorc()
        if x == 88:
            poluogre()
        if x == 1:
            print('Вы выбрали Человека\n')
            char['Ловкость'] = 2
            char['Сила'] = 2
            char['Ловкость'] = 2
            char['Обаяние'] = 2
            char['Технология'] = 2
            char['Магия'] = 2
            break
        if x == 2:
            print('Вы выбрали Ельфа\n')
            char['Ловкость'] = 2
            char['Обаяние'] = 2
            char['Магия'] = 2
            char['Здоровье'] = 90
            break
        if x == 3:
            print('Вы выбрали Карлика\n')
            char['Ловкость'] = 1
            char['Сила'] = 2
            char['Обаяние'] = 1
            char['Технология'] = 2
            char['Здоровье'] = 110
            break
        if x == 4:
            print('Вы выбрали Гнома\n')
            char['Здоровье'] = 80
            char['Обаяние'] = 3
            break
        if x == 5:
            print('Вы выбрали Хоббита\n')
            char['Ловкость'] = 3
            break
        if x == 6:
            print('Вы выбрали Полуэльфа\n')
            char['Обаяние'] = 2
            char['Ловкость'] = 2
            char['Магия'] = 2
            break
        if x == 7:
            print('Вы выбрали Полуорка\n')
            char['Обаяние'] = 0
            char['Сила'] = 5
            char['Здоровье'] = 120
            break
        if x == 8:
            print('Вы выбрали Полуогра\n')
            char['Здоровье'] = 130
            char['Сила'] = 6
            char['Защита'] = 2
            break
    name = input('\nВведите имя: ')
    return name