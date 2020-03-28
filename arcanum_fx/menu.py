import os
def menu():
    print('1. Сохранить игру')
    print('2. Продолжить')
    print('3. Выйти из игры\n')
    x = int(input('Введите цифру: '))
    os.system('cls' if os.name == 'nt' else 'clear')
    return x