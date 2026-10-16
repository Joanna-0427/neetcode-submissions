class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(i,j):
            while 0 <= i <= j < n:
                if s[i] != s[j]:
                    return s[i+1:j]
                i -= 1
                j += 1
            return s[i+1:j]
        
        maxleng = 0
        res = ''
        #s = "ababd" [a,ab之间，b，ba之间，a，ab之间，b，bd之间，d]
        for m in range(2*n-1):
            l = m//2
            r = l + m%2
            cur = expand(l,r)
            if len(cur) > maxleng:
                res = cur
                maxleng = len(cur)
        
        return res

        


