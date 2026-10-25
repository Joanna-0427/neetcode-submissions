class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False
        target = total // 2

        n = len(nums)
        dp = [False] * (target+1)
        dp[0] = True
        
        for num in nums:
            for s in range(target,num-1,-1): #倒序防止s-num元素会重复用；如果正序，先更新num；在更新比num大的数，这样num可能用了2次
                if dp[s-num]: #target依赖更小的和，把所有能更新的子问题更新一遍，从[num,target]-num 即[0,target-num]更新一遍
                    dp[s] = True
                if dp[target]:
                    return True
        return dp[target] #只要target有一组在，分成两组另一组也在

