from menu import Menu
from simpleMenuIItem import Simple_menu_item
from fx import *
from menuItem import Menu_item

main_menu = Menu()

file_menu = main_menu.addSubMenu('File')
file_menu.addItems('Create', foo)
file_menu.addItems('Open',foo)

edit_menu = main_menu.addSubMenu('Edit')
edit_menu.addItems('Return',foo)


#лист стюдентс комманд это классы? я думал это функции которые мы будем как параметр в меню, чтобы делали свою работу
main_menu.addItems('Показать студентов',listStudents)
main_menu.addItems('Показать неуспевающих',showLow)
main_menu.addItems('Показать отличников',showHight)
main_menu.addItems('Добавить студента',addStudent)
main_menu.addItems('удалить студента',deleteStudent)


main_menu.run()


#Создать статические методы класса Program, отвечающие за следующие пункты главного меню:
#
#- список студентов
#- добавить студента
#- удалить студента
#- показать отличников
#- показать неуспевающих#
#
#В этих функциях использовать класс StudentRegistry для управления списком студентов. Добавить эти функции в меню как реализацию пунктов SimpleMenuItem.