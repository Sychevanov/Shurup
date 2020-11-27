# class Dialogs():
#     def __init__(self):
#         self.__listSayChar = None
#         self.__listSayMob = None

#     def getSay(self):
                        # 0                               1                           2
listSayChar = [
['добрый положительныйChar  1',"добрый ПолодительныйChar  2","добрый положительныйChar  3"],    #0
['злой положительныйChar  1',"злой ПолодительныйChar  2","злой положительныйChar  3"],          #1
['недоверчивыйChar  1',"недоверчивыйChar  2","недоверчивыйChar  3"],                            #2
['отрицательныйChar  1',"отрицательныйChar  2","отрицательныйChar  3"],   
]                      #3

listSayMob = [                        # 0                               1                              2
['добрый положительныйMob  1',"добрый ПолодительныйMob  2","добрый положительныйMob  3"] ,   #0
['злой положительныйMob  1',"злой ПолодительныйMob  2","злой положительныйMob  3"]      ,    #1
['недоверчивыйMob  1',"недоверчивыйMob  2","недоверчивыйMob  3"]           ,                 #2
['отрицательныйMob  1',"отрицательныйMob  2","отрицательныйMob  3"]       ,                  #3
]



for i in range(0,3):
    for j in range(0,4):
        print(j+1,'',listSayChar[j][i])
    x = int(input('\nВведите ответ: '))
    print('')
    y = i
    print(listSayMob[x-1][y])
    print('')