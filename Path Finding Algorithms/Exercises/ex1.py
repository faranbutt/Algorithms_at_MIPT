from heapq import heappush, heappop

def dijkstra(N, G, s, h):
    inf = float('inf')
    dist = [inf] * N
    parent = [-1] * N
    visited = [False] * N
    dist[s] = 0


    pq = []
    heappush(pq, (0, s))

    while pq:
        d, v = heappop(pq)

        if visited[v]:
            continue
        visited[v] = True

        for u, weight in G[v]:
            if dist[v] + weight < dist[u]:
                dist[u] = dist[v] + weight
                parent[u] = v
                heappush(pq, (dist[u], u))

    return dist, parent

def reconstruct_path(parent, s, h):
    path = []
    current = h
    while current != -1:
        path.append(current)
        current = parent[current]
    if path[-1] != s:
        return []
    return path[::-1]

if __name__ == "__main__":
    N, M = map(int, input().split())
    s, h = map(int, input().split())


    G = [[] for _ in range(N)]
    for _ in range(M):
        x, y, weight = map(int, input().split())
        G[x].append((y, weight))
        G[y].append((x, weight))
    dist, parent = dijkstra(N, G, s, h)

    if dist[h] == float('inf'):
        print(-1)
    else:
        path = reconstruct_path(parent, s, h)
        print(dist[h])
        print(len(path))
        print(' '.join(map(str, path)))



