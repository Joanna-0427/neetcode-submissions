class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxheap = []
        for i in range(n):
            heapq.heappush(maxheap,nums[i])
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        
        return maxheap[0]
        