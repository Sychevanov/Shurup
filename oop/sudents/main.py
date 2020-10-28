from menu import Menu
from simpleMenuIItem import Simple_menu_item
from menuItem import Menu_item
from program import Program
from studentRegistry import StudentRegistry
StudentRegistry().load()
main_menu = Menu()

main_menu.addItems('Cписок студентов',Program.listStudentsCommand) 
main_menu.addItems('Добавить студента',Program.addStudentCommand)

edit_menu = main_menu.addSubMenu("Редактировать студента")
edit_menu.addItems('Изменить Фамилию',Program.EditLastNameCommand)
edit_menu.addItems('Изменить имя',Program.EditFirstNameCommand)
edit_menu.addItems('Изменить отчество',Program.EditMidlleNameCommand)
edit_menu.addItems('Изменить группу',Program.EditGroupNameCommand)
edit_menu.addItems('Добавить оценку',Program.AddMarksCommand)
edit_menu.addItems('Удалить оценку',Program.DeleteMarksCommand)
edit_menu.addItems('Изменить оценку',Program.EditMarksCommand)
edit_menu.setStartupCommand(Program.SelectStudentCommand)
edit_menu.setBeforeCommand(Program.ShowSelectedCommand)
edit_menu.setTearDownCommand(Program.DeselectStudentCommand)

main_menu.addItems('Удалить студента',Program.removeStudentCommand)
main_menu.addItems('Показать отличников',Program.showHighAchiversCommand)
main_menu.addItems('Показать неуспевающих',Program.showLowArchiversCommand)#ntcn



main_menu.run()
StudentRegistry().save()


