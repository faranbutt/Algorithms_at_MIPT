def bisect(arr,key):
    left,right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid
    return left


def lis(N, arr):
    d = [float('inf')] * (N+1)
    d[0] = float('-inf')
    for num in arr:
        idx = bisect(d,num)
        if d[idx-1] < num < d[idx]:
            d[idx] = num
    return max(i for i in range(N+1) if d[i] < float("inf"))
        
if __name__=="__main__":
    N = int(input())
    array = list(map(int,input().split()))
    longest_subseq = lis(N,array)
    print(longest_subseq)
            
    
            
        
            

             
            
        
            