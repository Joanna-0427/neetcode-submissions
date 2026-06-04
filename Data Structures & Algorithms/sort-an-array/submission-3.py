import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        def heapify(arr,n,i):
            l = 2 * i + 1
            r = 2 * i + 2
            largest = i
            if l < n and arr[l] > arr[largest]:
                largest = l
            if r < n and arr[r] > arr[largest]:
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr,n,largest)
        
        def heapsort(arr):
            n = len(arr)
            for i in range(n//2-1, -1, -1):
                heapify(nums,n,i)
            
            for j in range(n-1,0,-1):
                nums[0], nums[j] = nums[j], nums[0]
                heapify(nums,j,0)

        heapsort(nums)
        return nums
            



        