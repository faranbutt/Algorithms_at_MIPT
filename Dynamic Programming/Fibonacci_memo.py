from time import time
memo = {0:0,1:1}
def fib_memo(n):
    mem = [0,1]
    print(mem)
    for i in range(2,n+1):
        mem.append(mem[-2]+mem[-1])
    return mem[-1]
start  = time()
a = fib_memo(40)
print(a)

end = time()
print(f'Time to execute is {end-start}')

