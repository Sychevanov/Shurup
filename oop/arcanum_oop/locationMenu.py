from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo
from newGame import newGame
from picture_draw import zastavka, dirijable, virdgil, mashin
from ArcanumMainMenu import ArcanumMainMenu
from Dialogs import dialogVirgil

location_menu = Menu(title="Разрушенный дирижабль")
location_menu.setStartupCommand(dirijable)
location_menu.setStartupCommand(dialogVirgil)
location_menu.addItems('Осмотреть кого-нибдуь',foo)
somewhere_menu = location_menu.addSubMenu('Идти куда-нибудь')
somewhere_menu.addItems('Сдлеать что-нибдуь где нибудь_1',foo)
somewhere_menu.addItems('Сдлеать что-нибдуь где нибудь_2',foo)
location_menu.addItems('Бой с кем-нибудь',foo)
location_menu.addItems('Журнал',foo)
infoChar_menu = location_menu.addSubMenu('О персонаже')
infoChar_menu.addItems('Харакатерисики',foo)
infoChar_menu.addItems('Сумка',foo)
infoChar_menu.addItems('Инвертарь',foo)

#ArcanumMainMenu().addLocMenu(location_menu)
#ArcanumMainMenu().locRun()
    