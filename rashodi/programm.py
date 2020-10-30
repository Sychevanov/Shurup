import json 
from Product import Product
from ProductCattegory import ProductCattegory
def save():
    products ={}
    for key in ProductCattegory().products().keys():
        for p in ProductCattegory().products()[key]:
            products[key] = []
            products[key].append(productInDict(p))
    
        
    with open ('products.json','w') as f:
        json.dump(products, f)

def load():
    with open ('products.json','r') as f:
        products2 = json.load(f)
        dictInproduct(products2)


def productInDict(p):
    productDict = []
    productDict.append(p.name)  
    productDict.append(p.price)
    return productDict

def dictInproduct(productInDict):
    for key in productInDict.keys():
        for i in  range(0,len(productInDict[key])):
            ProductCattegory().products()[key] = [Product(productInDict[key][i][0],productInDict[key][i][1])]



