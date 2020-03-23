def proverka(s,n1,n2):
    while True:
        x = input(s)
        try:
            x = int(x)
            if x >= n1 and x <= n2:
                break
            else: 
                print(f'Введите число от {n1} до {n2}')
        except:
            print('Введите цифру, а не букву')    
    return x