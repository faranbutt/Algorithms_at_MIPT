if __name__ == "__main__":
    N,s,f,K= map(int,input().split())
    a = []
    for i in range(N):
        a.append(list(map(int,input().split())))
    d = [[float("inf")] * N for i in range(K+1)]
    d[0][s] = 0
    for k in range(1,K+1):
        for u in range(N):
            for v in range(N):
                if a[u][v] != -1:
                    d[k][v] = min(d[k][v],d[k-1][u]+a[u][v])
    result = min(d[k][f] for k in range(1,K+1))
    print(-1 if result == float('inf') else result)
