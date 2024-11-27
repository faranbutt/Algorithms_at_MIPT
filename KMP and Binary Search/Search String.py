s = 'ababacababa'
p = 'aba'

N = len(s)
K = len(p)

indexes = []
for i in range(N-K+1):
    if all([s[i+j] == p[j] for j in range(K)]):
        indexes.append(i)
print(indexes)