class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        def expand(l,r):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            return count

        res = 0
        for i in range(2*n-1):
            l = i // 2
            r = l + i % 2
            count = expand(l,r)
            res += count
        
        return res


