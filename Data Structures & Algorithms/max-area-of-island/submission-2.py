class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        rows, cols = len(grid),len(grid[0])
        area = 0

        def dfs(i,j):
            nonlocal area
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return 
            

            area += 1
            grid[i][j] = 0
            
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    #area是外层变量，会持续累积，需要在每次计算时候清0
                    area = 0
                    dfs(i,j)
                    maxarea = max(area,maxarea)
        
        return maxarea
        
