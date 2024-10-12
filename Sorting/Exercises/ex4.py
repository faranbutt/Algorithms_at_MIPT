arr = [5,1,2,55,16,713,23,22,3]

def bubble_sort(arr):
    N = len(arr)
    for i in range(N):
        for j in range(0,N-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr
print(bubble_sort(arr))

def selection_sort(arr):
    N = len(arr)
    for i in range(N):
        i_min = i
        for j in range(i+1,N):
            if arr[i] > arr[j]:
                i_min = j
        arr[i_min],arr[i] = arr[i], arr[i_min]
    return arr
print(selection_sort(arr))

def insertion_sort(arr):
    N = len(arr)
    for i in range(1,N):
        key = arr[i]
        j = i-1
        while j >= 0 and  key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
print(insertion_sort(arr))
