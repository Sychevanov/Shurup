class AllProductCattegory():
    def __init__(self):
        self.__allProductCattegory = []
    

    def allProductCattegory(self):
        return self.__allProductCattegory
    

    def printCattegory(self):
        if len(self.__allProductCattegory) != 0:
            for i in range(0, len(self.__allProductCattegory)):
                print(i, '. ', self.__allProductCattegory[i].name)
                print(len(self.__allProductCattegory)+1, ' Новая каттегория')
        else:
            print('СОздайте каттегорию: ')

