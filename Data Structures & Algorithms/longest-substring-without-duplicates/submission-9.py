class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        n = len(s)
        maxsub = 0
        visited = set()

        for j in range(n):
            while s[j] in visited:
                visited.remove(s[i])
                i += 1
            
            visited.add(s[j])
            maxsub = max(maxsub,j-i+1)
        
        return maxsub
