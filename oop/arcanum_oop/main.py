from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from fx import foo
from picture_draw import zastavka
from Create_char import *
main_menu = Menu()
main_menu.setStartupCommand(zastavka)


newGame_menu = main_menu.addSubMenu("Новая игра",False)



newGame_menu.setStartupCommand(create)
newGame_menu.addItems('Начать игру с этим персонажем',foo)
newGame_menu.addItems('Изменить персонажа',foo)

main_menu.addItems('Загрузить игру(В разработке)',foo)
#стартап команд для того чтобы был вызов функции до пеачться меню



#edit_menu.addItems('Изменить Фамилию',foo)
#edit_menu.addItems('Изменить имя',foo)
#edit_menu.addItems('Изменить отчество',foo)
#edit_menu.addItems('Изменить группу',foo)
#edit_menu.addItems('Добавить оценку',foo)
#edit_menu.addItems('Удалить оценку',foo)
#edit_menu.addItems('Изменить оценку',foo)
#edit_menu.setStartupCommand(Program.SelectStudentCommand)
#edit_menu.setBeforeCommand(Program.ShowSelectedCommand)
#edit_menu.setTearDownCommand(Program.DeselectStudentCommand)

#main_menu.addItems('Удалить студента',foo)
#main_menu.addItems('Показать отличников',foo)
#main_menu.addItems('Показать неуспевающих',foo)


main_menu.run()


