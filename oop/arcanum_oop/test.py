import os
#from arcanum_fx.vibor_char import human,elf,dwarf,gnome,hobbit,poluelf,poluorc,poluogre
#from arcanum_fx.char import char
#from arcanum_fx.items_mob import items, snaryajenie
#from arcanum_fx.proverka import proverka


from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo, printChar, human
from picture_draw import zastavka


main_menu = Menu()
main_menu.addSubMenu('1')
main_menu.addItemsChar("char1")
main_menu.run()
print(char)