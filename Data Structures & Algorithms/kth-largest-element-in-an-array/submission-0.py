class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        l = len(nums) - k
        while l > 0:
            heapq.heappop(nums)
            l -= 1
        
        return nums[0]
        