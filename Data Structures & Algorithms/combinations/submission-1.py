class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(i,count):
            if count == k:
                res.append(path[:])
                return
            
            if i > n:
                return
            path.append(i)
            dfs(i+1,count+1)
            path.pop()
            dfs(i+1,count)
        
        dfs(1,0)
        return res
            