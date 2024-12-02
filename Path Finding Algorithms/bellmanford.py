def get_cycle(p,v):
    for i in range(len(p)):
        v = p[v]
    cycle = [v]
    cycle_start = v
    v = p[v]
    while v != cycle_start:
        cycle.append(v)
        v = p[v]
    cycle.append(cycle_start)
    return cycle[::-1]




def bellman_ford(N,E,s):
    d = [float('inf')] * N
    d[s] = 0
    p = [-1] * N
    for i in range(N-1):
        for (v,u,w) in E:
            if d[u] > d[v] + w:
                d[u] = d[v] + w
                p[u] = v
    for (v,u,w) in E:
        if d[u] > d[v] + w:
            p[u] = v
            print("Negative Cycle")
            c = get_cycle(p,u)
            print(len(c))
            print(' '.join(map(str,c)))
            return None
    return d

if __name__=="__main__":
    N,M = map(int,input().split())
    E = []
    for i in range(M):
        E.append(tuple(map(int,input().split())))
    s = int(input())
    d = bellman_ford(N,E,s)
    if d is not None:
        print(' '.join(map(str,d)))




