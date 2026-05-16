class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        cur = 0

        for n in range(0,len(nums)):
            if cur < 0:
                cur = 0
            cur += nums[n]
            maxsum = max(maxsum,cur)
        return maxsum
            