class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(idx):
            if len(path) == k:
                res.append(path[:])
                return
            
            for i in range(idx,n+1):
                path.append(i)
                dfs(i+1)
                path.pop()
        
        dfs(1)
        return res
