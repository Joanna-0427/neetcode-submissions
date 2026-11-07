class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        ocean = set()

        def dfs(r,c,prevheight,ocean):
            if r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prevheight or (r,c) in ocean:
                return
            
            ocean.add((r,c))
            dfs(r+1,c,heights[r][c],ocean)
            dfs(r-1,c,heights[r][c],ocean)
            dfs(r,c+1,heights[r][c],ocean)
            dfs(r,c-1,heights[r][c],ocean)
        
        pac = set()
        atla = set()
        for i in [0,rows-1]:
            for j in range(cols):
                if i == 0:
                    dfs(i,j,float('-inf'),pac)
                if i == rows-1:
                    dfs(i,j,float('-inf'),atla)
        
        for i in range(rows):
            for j in [0,cols-1]:
                if j == 0:
                    dfs(i,j,float('-inf'),pac)
                if j == cols-1:
                    dfs(i,j,float('-inf'),atla)

        res = []
        for r, c in pac:
            if (r,c) in atla:
                res.append([r,c])

        return res

        



            
            
