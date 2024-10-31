N = int(input())
q= []
for i in range(N):
    q.append([])

inp = list(input().split())
i = inp[0]

while i != '#':
    s = int(inp[1])
    if i == '+':
        q[s].append(int(inp[-1]))
    elif i == '-':
        print(q[s][0])
        q[s].pop(0)
    elif i == '!':
        length = len(q[s])
        middle = int(length / 2) + length % 2
        q[s].insert(middle, int(inp[-1]))
    elif i == '?':
        print(len(q[s]))

    inp = list(input().split())
    i = inp[0]
