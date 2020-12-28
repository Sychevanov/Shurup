from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo
from newGame import newGame
from picture_draw import zastavka
from locationMenu import location_menu, location_menu2
from ArcanumMainMenu import ArcanumMainMenu


main_menu = Menu(title='',flag=True,noBack=True,forsedExit = False)
main_menu.setStartupCommand(zastavka)
main_menu.addItems("Новая игра",newGame) 
main_menu.addItems('Загрузить игру(В разработке)',foo)

ArcanumMainMenu().addMainMenu(main_menu)
ArcanumMainMenu().addMainMenu(location_menu)



ArcanumMainMenu().mainRun()
