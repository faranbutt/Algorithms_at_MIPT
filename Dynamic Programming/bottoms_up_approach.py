def fab(n):
    arr = [None] * (n+1)
    arr[0] = 0
    arr[1] = 1
    for i in range(2,n+1):
        arr[i] = arr[i-1] + arr[i-2]

    return arr
print(fab(40))