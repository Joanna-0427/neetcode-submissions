class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        def dfs(idx):
            if idx >= len(s):
                res.append(path[:])
                return
            
            for i in range(idx,len(s)):
                part = s[idx:i+1]
                if not self.is_palindrome(part):
                    continue
                path.append(part)
                dfs(i+1)
                path.pop()
        dfs(0)
        return res


    def is_palindrome(self,s):
        l, r = 0, len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True