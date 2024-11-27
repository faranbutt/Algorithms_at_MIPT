n, m = map(int, input().split())

mm = [[1] * m for _ in range(n)]
g = [[] for _ in range(n * m)]

start_point, finish_point = -1, -1

for i in range(n):
    row = input()
    for j, cell in enumerate(row):
        if cell == 'E':
            start_point = i * m + j
        elif cell == 'X':
            finish_point = i * m + j
        elif cell == '#':
            mm[i][j] = 0

        if cell != '#':
            if i > 0 and mm[i - 1][j] == 1:
                g[i * m + j].append((i - 1) * m + j)
                g[(i - 1) * m + j].append(i * m + j)
            if j > 0 and mm[i][j - 1] == 1:
                g[i * m + j].append(i * m + j - 1)
                g[i * m + j - 1].append(i * m + j)

l = [-1] * (n * m)

def bfs(a):
    l[a] = 0
    queue = [a]
    while queue:
        current = queue.pop(0)
        for neighbor in g[current]:
            if l[neighbor] == -1:
                l[neighbor] = l[current] + 1
                queue.append(neighbor)

bfs(start_point)
print(l[finish_point])
