def left_binary_search(arr,target):
   l = 0
   r = len(arr)
   while l < r:
       mid = l + (r-l)//2
       if arr[mid] < target:
           l = mid + 1
       else:
           r = mid
   return l



def right_binary_search(arr,target):
   l = 0
   r = len(arr)
   while l < r:
       mid = l + (r -  l)//2
       if arr[mid] <= target:
            l = mid + 1
       else:
           r = mid
   return l



def find_range(tups,scores):
    scores.sort()
    results = []
    for left, right in tups:
        left_i = left_binary_search(scores,left)
        right_i = right_binary_search(scores,right)
        results.append(right_i - left_i)
    return results


if __name__=="__main__":
    N, M = map(int, input().split())
    scores = list(map(int, input().split())) if N > 0 else []
    tups = [tuple(map(int,input().split())) for _ in range(M)]
    results = find_range(tups,scores)
    for result in results:
        print(result)

