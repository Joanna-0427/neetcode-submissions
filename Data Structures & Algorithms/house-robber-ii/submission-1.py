class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp1 = [0] * n
        dp1[0] = 0
        dp1[1] = nums[0]
        for i in range(2,n):
            dp1[i] = max(dp1[i-1],dp1[i-2] + nums[i-1])
        

        dp2 = [0] * n
        dp2[0] = 0
        dp2[1] = nums[1]
        for j in range(2,n):
            dp2[j] = max(dp2[j-1],dp2[j-2] + nums[j])
        
        return max(dp2[-1],dp1[-1])
