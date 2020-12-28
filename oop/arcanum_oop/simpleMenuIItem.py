from menuItem import Menu_item
class Simple_menu_item(Menu_item):

    def __init__(self,title,foo, flag = True, printText = ''):       
        super().__init__(title)
        self.__foo = foo
        self.flag = flag
        self.printText = printText

    def run(self):
        if self.printText != '' and self.flag != None :
            print(self.printText)
        if self.flag != None:
            self.__foo()
        if self.flag == False :
            self.editTitle()
            self.flag = None

