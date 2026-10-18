class Solution:
    def numSquares(self, n: int) -> int:
        square = [k*k for k in range(1,int(n**0.5)+1)]
        m = len(square)
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        for k in range(m+1):
            dp[k][0] = 0

        for k in range(1,m+1):
            sq = square[k-1]
            for i in range(1,n+1):
                dp[k][i] = dp[k-1][i]
                if i >= sq:
                    dp[k][i] = min(dp[k][i],dp[k][i-sq] + 1)

        
        return dp[m][n]