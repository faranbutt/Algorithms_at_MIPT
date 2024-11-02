from time import time
start = time()



def stairs_rec(arr):
    if len(arr) <= 2:
        return arr[-1]
    
    d1 = arr[0] + stairs_rec(arr[1:])
    d2 = arr[1] + stairs_rec(arr[2:])
    
    return min(d1,d2)
arr  = [23,1,2,3,100,1]

min_cost = stairs_rec(arr)
print(min_cost)

end = time()
print(f"Total Time Taken is {end-start} ")
    
    
