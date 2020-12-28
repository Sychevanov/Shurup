from singletone import Singleton
class ArcanumMainMenu(metaclass=Singleton):
    def __init__(self):
        self.listMenu = []


    def addMainMenu(self,menu):
        self.listMenu.append(menu)
        self.menu = menu

    def mainRun(self):
        for menu in self.listMenu:
            menu.run()
    def map(self):
        for i, menuTitle in enumerate(self.listMenu[1:]):
            print(i+1, menuTitle.get_title())
        x = int(input('Выберите Локацию, куда хотите перейти: '))
        self.menu.forsedExit = False
        print('выход')
        self.listMenu[x].run()

    # def locRun(self):
    #     for menu in self.__listLocMenu:
    #         menu.run()

# for i,item in enumerate(self.__char.bag): #доделать, меню"что сделать с предметом" выкинуть, надеть, почитать описание и тд"
#             print(i+1, end='')
#             item.printName()
