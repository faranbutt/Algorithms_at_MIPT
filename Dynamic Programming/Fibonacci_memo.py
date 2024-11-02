memo  = {0:0,1:1}
def fib(n):
    if n<2:
        return n
    
    return fib(n-1) + fib(n-2)
    
    
inp =  int(input())
fibs = [fib(i) for i in range(inp)]
print(fibs)

    

