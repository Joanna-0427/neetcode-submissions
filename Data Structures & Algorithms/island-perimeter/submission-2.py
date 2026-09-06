class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])

        visited = set()
        perim = 0

        def dfs(i,j):
            nonlocal perim
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                perim += 1
                return
            
            if (i,j) in visited:
                return
            
            #全局变量perim累积，不需要返回值蹭蹭层层传递
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in visited:
                    dfs(i,j)
        #全局变量perim累积，不需要返回值蹭蹭层层传递
        return perim

