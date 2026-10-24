class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        words = set(dictionary)
        dp = [0] * (n+1)

        for i in range(1,n+1):
            dp[i] = dp[i-1] + 1 #放在内存循环会被dp[i]每轮都被覆盖
            for j in range(i):
                if s[j:i] in words:
                    dp[i] = min(dp[i],dp[j])
                
        
        return dp[-1]

            