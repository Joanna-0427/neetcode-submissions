class Solution:
    def numSquares(self, n: int) -> int:
        square = [i * i for i in range(1,int(n**0.5)+1)]
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1,n+1):
            for j in range(1,int(i**0.5)+1):         # digit = i ** 0.5  #4 ** 0.5 = 2.0永远float
                if j ** 2 <= i:
                    dp[i] = min(dp[i],dp[i-j*j]+1) #最优解不一定是最大的平方和，可能存在于最小的平方和
            
        return dp[n]
            
            