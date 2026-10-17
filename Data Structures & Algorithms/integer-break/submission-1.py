class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n+1)

        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(dp[i],j * dp[i-j],j*(i-j)) #每个i需要包含不拆的情况j*（i-j）也是两段
        
        return dp[n]

