N, M = map(int, input().split())
arr = list(map(int, input().split()))

def finded_pair(x, n, m, mid):
    count = 1
    o = x[0]
    for i in range(1, n):
        if x[i] >= o + mid:
            count += 1
            if count == m:
                return True
            o = x[i]
    return False

if M == 0:
    print(0)
    exit()

def binary_search(x, n, m, l, r):
    sol = 0
    while l <= r:
        mid = l + (r - l) // 2
        if finded_pair(x, n, m, mid):
            sol = max(sol, mid)
            l = mid + 1
        else:
            r = mid - 1
    return sol

arr.sort()
print(binary_search(arr, N, M, 0, arr[N - 1] - arr[0]))

