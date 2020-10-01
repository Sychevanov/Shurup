from abc import ABCMeta, abstractmethod
eat = 0
alcohol = 0
products = []
allProducts = [{'Продукты': eat}, {'Алкоголь': alcohol}]
#class Products(metaclass=ABCMeta):
class Product():
    def __init__(self,name,price):
        #self.products = []
        self.__name = name
        self.__price = price 

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,price):
        self.__price = price

    
    #def add(self,product):
    #    self.products.append(product)
        
def summ(products):
    summ = 0
    for product in products:
        summ = summ + product.price
        return summ


        

 



name = input('Введите наименование покупки: ')
price = int(input('Введите цену покупки: '))

products.append(Product(name,price))
found = False
for i in range(0,len(allProducts)):  #если имя товара не равно каждому кею из словаря тогда нужно создать категорию и засунть эксземпляр класса товара в эту каттегорию
    if name == list(allProducts[i].keys())[0]:
        found = True
        #allProducts.append({name:price})
    else:
        print('Выберите каттегорию: ')
if not found:#создать категорию
    allProducts.append({name:price})

print(products[0].price)

print(summ(products))
print (allProducts)