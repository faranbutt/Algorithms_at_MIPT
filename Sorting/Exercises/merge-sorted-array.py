def sort(nums1):
    if len(nums1) > 1:
        mid = int(len(nums1) / 2)
        left = nums1[:mid]
        right = nums1[mid:]
        sort(left)
        sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums1[k] = left[i]
                i += 1
            else:
                nums1[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums1[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            nums1[k] = right[j]
            j+=1
            k+=1

def merge(nums1,nums2,m,n):
    if m == 0 or n == 0:
        pass
    len_of_array = len(nums1)
    arr = []
    count = 0
    for i in range(m,len_of_array):
        nums1[m] = nums2[count]
        count += 1
        m+=1
    sort(nums1)


nums1 = [4,0,0,0,0,0]
nums2 = [1,2,3,5,6]
m = 1
n = 5
merge(nums1,nums2,m,n)
