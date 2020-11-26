from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo
from newGame import newGame
from picture_draw import zastavka
from locationMenu import location_menu


main_menu = Menu(title='',flag=True,noBack=True,forsedExit = False)
main_menu.setStartupCommand(zastavka)
main_menu.addItems("Новая игра",newGame)
main_menu.addItems('Загрузить игру(В разработке)',foo)
main_menu.run()

game_menu = Menu()
game_menu.addItems('Продолжить игру',location_menu)
game_menu.addItems('Сохранить игру',foo)
game_menu.run()

