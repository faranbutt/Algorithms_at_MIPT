#Insertion Sort
arr = [5,1,3,8,2,6,4,7]
N = len(arr)
for i in range(1,N):
    key = arr[i]
    j = i - 1
    while j >= 0  and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
print(arr)
