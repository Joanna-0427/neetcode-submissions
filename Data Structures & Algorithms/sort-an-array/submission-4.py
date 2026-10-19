class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merger(arr,l,m,r):
            i,j,k = l, 0, 0
            left = arr[l:m+1]
            right = arr[m+1:r+1]
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                    i += 1
                else:
                    arr[i] = right[k]
                    k += 1
                    i += 1
            
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1
            
            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1
            
        def mergesort(arr,L,R):
            if L >= R:
                return
            mid = (L+R)//2
            mergesort(arr,L,mid)
            mergesort(arr,mid+1,R)
            merger(arr,L,mid,R)
        
        mergesort(nums,0,len(nums)-1)
        return nums

