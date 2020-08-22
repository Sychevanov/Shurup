a = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]    
xORo = ''

def win2(a):
    for k in range(3):
        if a[0][k] == a[1][k] == a[2][k] != ' ' :            
            return True
        if a[k][0]==a[k][1] == a[k][2] != ' ' :
            return True
    if a[0][0]==a[1][1]==a[2][2]!= ' ':
        return True
    if a[0][2]==a[1][1]==a[2][0]!= ' ':
        return True
        
    return False
for o in range(9):     
    if o%2==0:
        xORo = 'x'
    else:
        xORo = '0'
    x = int(input(f'игрок {xORo} Введите коокрдинату х: '))
    y = int(input(f'игрок {xORo} Введите коокрдинату y: '))
    while not(x>=0 and x<3 and y>=0 and y<3 and a[x][y]==' '):
        print('введите корректно!')
        x = int(input(f'игрок {xORo} Введите коокрдинату х: '))
        y = int(input(f'игрок {xORo} Введите коокрдинату y: '))
        o=o-1
    a[x][y]=xORo
    for i in range(3):
        for j in range(3):       
            print('+ - ', end = '')
        print('+')
        for j in range(3):      
            print(f'| {a[i][j]} ', end = '')                
        print('|')
    for j in range(3):       
        print('+ - ', end = '') 
    print('+')
    
    if win2(a):
        print(f'win player {xORo}')
        break
        
if o==8 and not win2(a):
    print('ничья')
 

