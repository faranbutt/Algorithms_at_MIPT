from time import time

def fib(n):
    if n<2 :
        return n
    else:
        return fib(n-1) + fib(n-2)
start = time()
n = 40
print(fib(n))

end = time()
print(f"Time taken for getting {n}th  number is  {end-start}")