from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo
from newGame import newGame
from picture_draw import zastavka
from Create_char import *

main_menu = Menu()
main_menu.setStartupCommand(zastavka)


main_menu.addItems("Новая игра",newGame)
main_menu.addItems('Загрузить игру(В разработке)',foo)



main_menu.run()


