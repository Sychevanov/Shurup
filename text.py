n = int(input('enter n: '))
with open ('test.txt','w') as f:
    for i in range(1,n+1):
        f.write(f'{str(i)} \n')
    
with open ('test2.txt','w') as y:
    for i in range(1,n+1):
        y.write(f'{str(i)} ')

with open ('test.txt','r') as f:
    while True:
        s = f.readline()
        if not s:
            break
        
        print(s)
print(s.split())
