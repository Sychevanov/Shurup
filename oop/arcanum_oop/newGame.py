from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo, printChar, human
from charRegystry import CharRegystry
def newGame():
    
    main_menu = Menu(title='',flag=True,noBack=False,forsedExit = False)
    main_menu.setStartupCommand(printChar)
    # human_menu = main_menu.addSubMenu('Человек',True)
    # human_menu.setStartupCommand(human)
    # #human_menu.addItems('Продолжить этой расой',createChar)
    # human_menu.addItemsChar('Человек')
    
    # #main_menu.addItems('Человек', foo)
    # #main_menu.addItems('Орк', foo)
    # human_menu.setNoExitCommand()
    main_menu.addItemsChar('Человек')
    main_menu.addItemsChar('Эльф')
    main_menu.addItemsChar('Карлик')
    main_menu.addItemsChar('Гном')
    main_menu.addItemsChar('Хоббит')
    main_menu.addItemsChar('Полуэльф')
    main_menu.addItemsChar('ПолуОрк')
    main_menu.addItemsChar('Полуогр')
    main_menu.run()
    
   
