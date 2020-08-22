import struct
bag = []
bag.append({'Старый меч':[1,4]})
bag.append({'Старый меч2':[1,4]})
bag.append({'Старый меч34':[1,4]})
bag.append({'Старый меч':[1]})
bag.append({'Старый меч':[5,4,6]})
def sortirovka(bag):
    found=False
    while not found:
      found = True
      for i in range(len(bag)-1):
          if len(list(bag[i].values())[0])>len(list(bag[i+1].values())[0]):
            bag[i],bag[i+1] = bag[i+1],bag[i]
            found = False
sortirovka(bag)
k1=0
k2=0
k3=0
for i in range(0,len(bag)):
    if len(list(bag[i].values())[0]) == 1:
        k1 = k1 +1
for i in range(0,len(bag)):
    if len(list(bag[i].values())[0]) == 2:
        k2 =k2+1
for i in range(0,len(bag)):
    if len(list(bag[i].values())[0]) == 3:
        k3 =k3+1
print(k1,k2,k3)


        



       
       
       


    