class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        res = 0
        def dfs(i,j):
            nonlocal res
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0 or (i,j) in visited:
                return
            
            res += 1 
            visited.add((i,j))  #全局dfsvisited不回溯；路径dfs回溯
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            

        maxval = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = 0
                    dfs(i,j)
                    maxval = max(res,maxval)
        
        return maxval
        