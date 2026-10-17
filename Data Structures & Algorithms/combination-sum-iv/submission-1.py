class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        dp = [0] * (target+1)
        dp[0] = 1
        res = 0

        for s in range(1,target+1):
            for n in nums:
                if s-n >= 0:
                    dp[s] += dp[s-n]
        
        return dp[target]