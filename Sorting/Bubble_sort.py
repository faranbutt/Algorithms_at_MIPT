arr =  [4, 1, 5, 3, 6, 2, 9, 7, 8]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
sorted_array = bubble_sort(arr)
print("Sorted Array:",sorted_array)

