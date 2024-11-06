
def turtle(mat):
    N,M = len(mat),len(mat[0])
    print(mat)
    d  = [[None] * M for i in range(N)]
    d[0][0] = mat[0][0]
    for j in range(1,M):
        d[0][j]  = d[0][j-1] + mat[0][j]
    for i in range(1,M):
        d[i][0] = d[i-1][0] + mat[i][0]
    for i in range(1,N):
        for j in range(1,M):
            d[i][j] = max(d[i-1][j],d[i][j-1]) + mat[i][j]
    return d[N-1][M-1]
     
    
mat = [[3,5,10,4],[1,1,6,2],[1,8,5,8],[1,8,3,2]]
food = turtle(mat)
print(f"Max food turtle can eat is {food}")