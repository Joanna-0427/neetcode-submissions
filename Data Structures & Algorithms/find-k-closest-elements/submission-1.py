class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    
        # minheap = []
        # for r in range(len(arr)):
        #     val = (-abs(arr[r] - x), -arr[r])
        #     heapq.heappush(minheap,val)
        #     if len(minheap) > k:
        #         heapq.heappop(minheap)
        
        # res = [-v for _, v in minheap]
        # res.sort()
        # return res

        l, r = 0, len(arr)-1
        while r - l + 1 > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            else:
                r -= 1
        return arr[l:r+1]


