from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo, beginLocation1, textLocation1
from newGame import newGame
from picture_draw import zastavka, dirijable, virdgil, mashin
from ArcanumMainMenu import ArcanumMainMenu
from Dialogs import dialogVirgil

location_menu = Menu(title="Разрушенный дирижабль")
location_menu.setStartupCommand(dirijable)
location_menu.setStartupCommand(dialogVirgil)
location_menu.setStartupCommand(beginLocation1)
location_menu.addItems('Осмотреть мертвого человека',foo)
somewhere_menu = location_menu.addSubMenu('Пройти вдоль разрушенного дирижабля')
somewhere_menu.setStartupCommand(textLocation1)
somewhere_menu.addItems('Войти в пещеру',foo)
somewhere_menu.addItems('Собрать рядом с пещерой цветы',foo)
location_menu.addItems('Напасть на волков',foo)

#эту часть вынести, чтобы всегда было меню о персонаже
infoChar_menu = location_menu.addSubMenu('О персонаже')
infoChar_menu.addItems('Харакатерисики',foo)
infoChar_menu.addItems('Журнал',foo)
infoChar_menu.addItems('Сумка',foo)
infoChar_menu.addItems('Инвертарь',foo)

#ArcanumMainMenu().addLocMenu(location_menu)
#ArcanumMainMenu().locRun()
    