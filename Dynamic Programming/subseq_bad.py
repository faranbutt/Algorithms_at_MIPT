'''
dynammic programming

subproblem => d[i] length if LIS which end in x[i]

Basis => d[0] = 1

inductive_step => d[i] =  d[j] + 1  if x[j] < x[i]  ; 1 otherwise


result => max(d[i]) steps
         0 <= i <= N
         
         
Time Complexity = O(n^2)

'''



def subseq(arr):
    N = len(arr)
    d = [0] * N
    d[0] = 1
    for i in range(1,N):
        max_d = 0
        for j in range(i):
            if arr[j] < arr[i] and d[j] > max_d:
                max_d = d[j]
        d[i] = max_d + 1
    return max(d)  
    
    
arr = [3,5,10,1,6,8,9,8]
max_sequence_val = subseq(arr)
print(f"The maximum subsequence we can get is {max_sequence_val}")