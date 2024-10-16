data = [0,2,1,1,0,1,0,0,2,3,5,3,4,2]
def sort(arr):
    n = len(arr)
    counter = dict()
    key = 0
    for i in range(n):
        if arr[i] not in counter:
            print(counter,key)
            if key > arr[i]:
                temp = counter.pop(key)
                counter[arr[i]] = 1
                counter[key] = temp
            key  = arr[i]
            counter[arr[i]]  = 1
        else:
            counter[arr[i]] += 1
    dummy = list()
    for key,value in counter.items():
        dummy.append([key] * value)
    print(dummy)
sort(data)
