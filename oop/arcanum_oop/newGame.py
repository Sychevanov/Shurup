import os
#from arcanum_fx.vibor_char import human,elf,dwarf,gnome,hobbit,poluelf,poluorc,poluogre
#from arcanum_fx.char import char
#from arcanum_fx.items_mob import items, snaryajenie
#from arcanum_fx.proverka import proverka


from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo, printChar, human, createChar
from picture_draw import zastavka
def newGame():
    
    main_menu = Menu(title='',flag=True,noBack=False,forsedExit = False)
    main_menu.setStartupCommand(printChar)
    human_menu = main_menu.addSubMenu('Человек',True)
    human_menu.setStartupCommand(human)
    human_menu.addItems('Продолжить этой расой',createChar)
    
    #main_menu.addItems('Человек', foo)
    #main_menu.addItems('Орк', foo)
    human_menu.setNoExitCommand()
    

    main_menu.run()
    