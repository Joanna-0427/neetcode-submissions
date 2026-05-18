class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        1. strs[0] as base element
        2. strs[0][i]walk through each character in each element 
        3. move until shortest to the end.
        O(m * n)
        """
        n = len(strs[0])
        for i in range(n):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        
        return strs[0]


                