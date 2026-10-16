class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for j in range(1,n+1): #j是表示长度，所以到n+1：长度为n
            for i in range(j):
                if dp[i] and s[i:j] in word_set:
                    dp[j] = True
                    break

                
                # i = j+1 #只考虑一个结果，不回头就是贪心
        return dp[-1]
            

