from ProductCattegory import ProductCattegory
class ProductRegistry():

    def printShort(self):
        for key in ProductCattegory().products().keys():
            print(key)
        key = input('Выберите каттегорию')
        if key in ProductCattegory().products().keys():
            