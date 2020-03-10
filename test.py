import random
bag = {'С уроном':[],
    'Без урона': {},
    'Метательное': [],
}

a = [{'нож': [2,2,90]}]
b = [{'нож2': [3,3,90]}]
bag['Метательное'].append([{'нож': [2,2,90]}])
bag['Метательное'].append(b)
print(bag['Метательное'])
bag['С уроном'].append([{'меч':[2,4]}])
print(bag)

for key in bag:
  print(bag[key].values())