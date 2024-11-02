array = [2,0,0,1,-1,-2,1,0]
def sorter(arr):
    n = len(arr)
    min_val = min(arr)
    max_val = max(arr)
    shift = -min_val
    m = max_val + shift + 1
    a = [0] * m
    print(a)
    for i in arr:
        a[i+shift] += 1
    print(a)
    for i in range(1,m):
        a[i] += a[i-1]
    print(a)
    res = [None] * n
    for i in range(n):
        position = a[arr[i]+shift]-1
        res[position] = arr[i]
        a[arr[i]+shift] -= 1
    print(res)
print(sorter(array))