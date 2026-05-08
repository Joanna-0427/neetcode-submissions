class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = float('-inf')
        cur = 0
        for n in nums:
            if cur < 0:
                cur = 0
            cur += n
            maxsub = max(maxsub,cur)
        return maxsub
            
            
                