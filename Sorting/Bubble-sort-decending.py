arr =  [4, 1, 5, 3, 6, 2, 9, 7, 8]
N = len(arr)
for i in range(N):
    for j in range(0,N-i-1):
        if arr[j] < arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]


print(arr)


