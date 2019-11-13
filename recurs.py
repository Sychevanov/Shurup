def fibonacci(n):
    if n == 1 or n == 2: # n in (1,2)
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
n = int(input('vvedite nomer fib:  ')) 
print(fibonacci(n))