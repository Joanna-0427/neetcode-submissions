class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1,amount+1):
            res = float('inf')
            for coin in coins:
                
                if 0 <= i - coin < i:
                    res = min(1 + dp[i-coin],res)
                    dp[i] = res
        
        return dp[amount] if dp[amount] != float('inf') else -1

