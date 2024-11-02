from time import time
start = time()


def paid_stair(arr):
    N = len(arr)
    d = [None] * N
    d[0] = arr[0]
    d[1] = arr[1]
    for i in range(2,N):
        d[i] = min(d[i-1],d[i-2]) + arr[i]

    return d[-1]  
    
arr  = [23,1,2,3,100,1]

min_cost = paid_stair(arr)
print(min_cost)

end = time()
print(f"Total Time Taken is {end-start} ")
    
    
