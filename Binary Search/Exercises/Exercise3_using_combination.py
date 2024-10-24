tup = []
def find_max_min(tup):
    min_distances = []

    for t in tup:
        n = len(t)
        min_dist = float('inf')
        for i in range(n):
            for j in range(i+1,n):
                distance = abs(t[i] - t[j])
                min_dist = min(distance,min_dist)
        min_distances.append(min_dist)
    return max(min_distances)

def combination(N,M,arr,index,data,i):
    if index == M:
        tup.append(data[:])
        return
    if i >= N:
        return
    data[index] = arr[i]
    combination(N,M,arr,index+1,data,i+1)
    combination(N,M,arr,index,data,i+1)


def print_comb(N,M,arr):
    data = list(range(M))
    combination(N,M,arr,0,data,0)
    max_min = find_max_min(tup)
    print(max_min)

N,M = map(int,input().split())
arr = list(map(int,input().split()))
print_comb(N,M,arr)