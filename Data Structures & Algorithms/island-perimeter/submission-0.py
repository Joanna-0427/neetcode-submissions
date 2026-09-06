class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])

        visited = set()

        def dfs(i,j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 1
            
            if (i,j) in visited:
                return 0
            
            visited.add((i,j))
            #或者提前初始化，perim=0，后面则perim+=dfs(i+1,j).
            perim = dfs(i+1,j)
            perim += dfs(i,j+1)
            perim += dfs(i-1,j)
            perim += dfs(i,j-1)

            return perim
        
        for i in range(rows):
            for j in range(cols):
                #dfs内部也能判断visited，但是在外层直接判断不进入循环，省时
                if grid[i][j] == 1 and (i,j) not in visited:
                    return dfs(i,j)