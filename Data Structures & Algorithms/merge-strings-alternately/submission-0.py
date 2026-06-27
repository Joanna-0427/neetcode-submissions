class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        p1, p2 = 0, 0
        res = ''
        while p1 < n1 and p2 < n2:
            res += word1[p1]
            res += word2[p2]
            p1 += 1
            p2 += 1
        
        if n1 - p1 > 0:
            res += word1[p1:]
        
        if n2 - p2 > 0:
            res += word2[p2:]
        return res

