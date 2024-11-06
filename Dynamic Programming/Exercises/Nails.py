def find_shortest_thread(N,cor):
    if N == 2:
        return abs(cor[0] - cor[1])
    else:
        d = [0] * (N-1)
        d[0] = abs(cor[0] - cor[1])
        d[1] = abs(cor[0] - cor[2])
        for i in range(3,N):
            d[i-1] = min(d[i-2],d[i-3]) + cor[i] - cor[i-1] 
    return d[-1]
    

if __name__=='__main__':
    N = int(input())
    cor = list(map(int, input().split()))
    cor.sort()
    st =  find_shortest_thread(N,cor)
    print(st)