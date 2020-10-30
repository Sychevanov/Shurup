from Product import Product
from programm import save,load
from ProductCattegory import ProductCattegory
from AllProductCattegory import AllProductCattegory
load()
while True:
    print('Если хотите выйти, напишите "Выход"\n: ')
    name = input('Введите наименование товара: ')
    if name == 'Выход':
        break
    prise = input('Введите цену товара: ')
    if prise == 'Выход: ':
        break
    
    ProductCattegory().add(Product(name,prise))

print(ProductCattegory().products())
save()