from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo, beginLocation1, textLocation1,infoChar_menu, textLocation2
from newGame import newGame
from picture_draw import zastavka, dirijable, virdgil, mashin
from ArcanumMainMenu import ArcanumMainMenu
from Dialogs import Dialog,VirgilChar,VirgilNPC
from charRegystry import CharRegystry
from fight import fight
from item import Item
import os

d = Dialog()

d.addDialog(VirgilNPC,VirgilChar)

location_menu = Menu(title="Разрушенный дирижабль",info=True)
location_menu.setStartupCommand(dirijable)
location_menu.setStartupCommand(d.run)
location_menu.setStartupCommand(beginLocation1)
location_menu.addItems('Осмотреть мертвого человека',CharRegystry().addRandItem, flag = False)

somewhere_menu = location_menu.addSubMenu('Пройти вдоль разрушенного дирижабля')

somewhere_menu.setStartupCommand(textLocation1)
somewhere_menu.addItems('Войти в пещеру',foo)
somewhere_menu.addItems('Собрать рядом с пещерой цветы',fight)



location_menu2 = Menu(title="Разрушенный дирижабль2",info=True)

location_menu2.addItems('Осмотреть мертвого человека2',foo)
somewhere_menu2 = location_menu2.addSubMenu('Пройти вдоль разрушенного дирижабля2')

somewhere_menu2.setStartupCommand(textLocation1)
somewhere_menu2.addItems('Войти в пещеру2',foo)
somewhere_menu2.addItems('Собрать рядом с пещерой цветы2',fight)





location_menu.add_existing_submenu(infoChar_menu())
location_menu2.add_existing_submenu(infoChar_menu())

