def KP(arr, n, m):
    d = [[0] * (m + 1) for i in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, m + 1):
            weight = arr[i - 1][0]
            value = arr[i - 1][1]
            if weight > w:
                d[i][w] = d[i - 1][w]
            else:
                d[i][w] = max(d[i - 1][w], d[i - 1][w - weight] + value)

    included_items = []
    w = m
    for i in range(N, 0, -1):
        if d[i][w] != d[i - 1][w]:
            included_items.append(i)
            w -= arr[i - 1][0]
    included_items.reverse()
    print(d[n][m])
    print(len(included_items))
    [print(i, end=' ') for i in included_items]


if __name__ == "__main__":
    M, N = map(int, input().split())
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    arr = [list(a) for a in zip(c, d)]
    KP(arr, N, M)

