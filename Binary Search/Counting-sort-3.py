data = [0,2,1,1,0,1,0,0,2]
def counting_sort(arr):
    N = len(arr)
    M = max(arr) + 1
    a = [0] * M
    for i in arr:
        a[i] += 1
    for i in range(1,M):
        a[i] += a[i-1]
    res = N * [None]
    for i in range(N):
        position = a[arr[i]]-1
        res[position] = arr[i]
        a[arr[i]] -= 1
    return res


print(counting_sort(data))