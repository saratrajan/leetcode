def fib(num):
    if(num >= 3):
        return fib(num - 1) + fib(num - 2)
    else:
        return 1    

print(fib(50))