
def memo(fn):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return wrapper
    
    
    
@memo    
def fib(n):
    if n<2:
        return n
    return fib(n-1) + fib(n-2)
    
    
    
    
    
inp =  int(input())
fibs = [fib(i) for i in range(inp)]
print(fibs)

    

