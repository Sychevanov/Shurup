from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo, beginLocation1, textLocation1,infoChar_menu
from newGame import newGame
from picture_draw import zastavka, dirijable, virdgil, mashin
from ArcanumMainMenu import ArcanumMainMenu
from Dialogs import dialogVirgil
from charRegystry import CharRegystry
from fight import fight
mob =1
location_menu = Menu(title="Разрушенный дирижабль",info=True)
location_menu.setStartupCommand(dirijable)
location_menu.setStartupCommand(dialogVirgil)
location_menu.setStartupCommand(beginLocation1)
location_menu.addItems('Осмотреть мертвого человека',foo)
somewhere_menu = location_menu.addSubMenu('Пройти вдоль разрушенного дирижабля')

somewhere_menu.setStartupCommand(textLocation1)
somewhere_menu.addItems('Войти в пещеру',foo)
somewhere_menu.addItems('Собрать рядом с пещерой цветы',fight)








location_menu.add_existing_submenu(infoChar_menu())

#ArcanumMainMenu().addLocMenu(location_menu)
#ArcanumMainMenu().locRun()
    