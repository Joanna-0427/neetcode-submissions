class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:return 0
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        dp = [0] * (n+1)
        dp[1] = nums[0]

        for i in range(2,n+1):
            #取一个最优值，状态只依赖前两项dp[i-1], dp[i-2] + nums[i-1],每一项都得到一个当前最优值
            dp[i] = max(dp[i-1],dp[i-2] + nums[i-1])
            #dp[i]表示0-i间的最优值，第i间可能偷，可能没偷
        
        return dp[-1]
