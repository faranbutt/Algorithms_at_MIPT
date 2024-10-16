arr = [2,5,10,22,100,123,235,300]
def Binary_Search_Recursive(x,key,left,right):
    if right >= left:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return Binary_Search_Recursive(x,key, mid + 1, right)
        else:
            return Binary_Search_Recursive(x,key,left, mid - 1)
    else:
        return -1




index = Binary_Search_Recursive(arr,100,0, len(arr) - 1)
print(index)
