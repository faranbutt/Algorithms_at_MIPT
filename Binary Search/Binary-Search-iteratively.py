arr = [1,2,4,5,10,11,22]
def binary_search(x,key):
    left = 0
    right = len(x) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if x[mid] == key:
            return mid
        elif x[mid] < key:
            left  = mid + 1
        else:
            right = mid - 1
    return -1

index = binary_search(arr,11)
print(index)