from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo, printChar, human
from charRegystry import CharRegystry
def newGame():
    
    main_menu = Menu(title='',flag=True,noBack=False,forsedExit = True)
    main_menu.setStartupCommand(printChar)

    main_menu.addItemsChar('Человек',main_menu)
    main_menu.addItemsChar('Эльф',main_menu)
    main_menu.addItemsChar('Карлик',main_menu)
    main_menu.addItemsChar('Гном',main_menu)
    main_menu.addItemsChar('Хоббит',main_menu)
    main_menu.addItemsChar('Полуэльф',main_menu)
    main_menu.addItemsChar('ПолуОрк',main_menu)
    main_menu.addItemsChar('Полуогр',main_menu)
    main_menu.run()
    
   
