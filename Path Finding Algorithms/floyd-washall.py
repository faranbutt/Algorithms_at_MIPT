if __name__ == '__main__':
    N = int(input())
    G = [{} for i in range(N)]
    E = []
    a = []
    for i in range(N):
        a.append(list(map(int,input().split())))
    d = [list(ai) for ai in a]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k]+d[k][j])
    for di in d:
        print(' '.join(map(str,di)))