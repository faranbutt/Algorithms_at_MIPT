from time import time

def fib(n):
    if n<2:
        return n
    
    return fib(n-1) + fib(n-2)
    
    
inp =  int(input())
fibs = [fib(i) for i in range(inp)]
print(fibs)

end = time()
print(f"Time taken for getting {n}th  number is  {end-start}")