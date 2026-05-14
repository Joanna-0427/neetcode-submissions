class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = i = 0
        maxsub = nums[0]
        n = len(nums)

        while i < n:
            if cur < 0:
                cur = 0
            cur += nums[i]
            maxsub = max(cur, maxsub)
            i += 1
        
        return maxsub