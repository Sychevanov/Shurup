from singletone import Singleton
class ArcanumMainMenu(metaclass=Singleton):
    def __init__(self):
        self.listMenu = []


    def addMainMenu(self,menu):
        self.listMenu.append(menu)


    def mainRun(self):
        for menu in self.listMenu:
            menu.run()
