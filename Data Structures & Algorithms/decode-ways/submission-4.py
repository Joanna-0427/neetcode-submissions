from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        @cache
        def dfs(idx):
            nonlocal res
            if idx >= len(s):
                return 1
            cnt = 0
            for i in range(idx,len(s)):
                part = s[idx:i+1]
                if int(part) > 26: #continue是跳过，但会继续尝试下一个，这时应该break
                    break
                if part.startswith('0'):
                    break
               
                cnt += dfs(i+1)
            return cnt

        return dfs(0)



