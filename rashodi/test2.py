from Product import Product
from programm import save
from ProductCattegory import ProductCattegory
from AllProductCattegory import AllProductCattegory

p = Product('Хлеьб',45)
ProductCattegory().add(p)

productDict = []
productDict.append(p.name)  
productDict.append(p.priсe)


products = {}
for key in ProductCattegory().products().keys():
    for p in ProductCattegory().products()[key]:
        products[key] = []
        products[key].append(productInDict(p))

    
with open ('products.json','w') as f:
    json.dump(products, f)

print(ProductCattegory().products())
