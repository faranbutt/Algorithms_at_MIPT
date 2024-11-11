def KS(n,x):
    total_profit = sum(x)
    if total_profit % 2 != 0:
        return "NO"
    target = total_profit // 2
    d = [False] * (target + 1)
    d[0] = True
    for cost in x:
        for j in range(target,cost-1,-1):
            d[j]  = d[j] or d[j-cost]
    return "YES" if d[target] else "NO"



if __name__ == "__main__":
    N = int(input())
    arr = list(map(int,input().split()))
    print(KS(N,arr))
