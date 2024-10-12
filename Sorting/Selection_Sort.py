arr =  [4, 1, 5, 3, 6, 2, 9, 7, 8]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i],arr[min_index] =arr[min_index],arr[i]
    return arr

sorted_array = selection_sort(arr)
print(sorted_array)