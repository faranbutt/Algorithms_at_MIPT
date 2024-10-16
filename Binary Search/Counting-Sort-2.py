data = [0,2,1,1,0,1,0,0,2]
def counting_sort(arr):
    N = len(arr)
    M = max(arr) + 1
    dummy = [0] * M
    for i in arr:
        dummy[i] += 1
    res = []
    for i in range(M):
        for j in range(dummy[i]):
            res.append(i)
    return res


sorted_array = counting_sort(data)
print(sorted_array)