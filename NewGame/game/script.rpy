# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.

# class Char():
#     def __init__(self,name):
#         self.__name = name
#     def getName():
#         return self.__name
init python:

    a = 45
    class Char():
        def __init__(self,name):
            self.name = name
        def getName():
            return self.__name
    ch = Char('чвуак')
    name = ch.name
# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.
define e = Character('Эйлин', color="#c8ffc8")
#define ch = Char('чвуак')
# Игра начинается здесь:
screen add_test():
    add "images/logo.png" xalign 1.0 yalign 0.0
label start:

    scene bg room

    show eileen happy

    e "Вы создали новую игру Ren'Py."

    e  "[a]"
    e '[ch.name]'
    $ name2 = ch.name
    show add_test
    e '[ch.name]'

    return
