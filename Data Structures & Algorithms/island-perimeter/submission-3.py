class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perim = 0
        visited = set()

        def dfs(r,c):
            nonlocal perim
            if (r,c) in visited:
                return
                
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                perim += 1
                return
            
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return perim
