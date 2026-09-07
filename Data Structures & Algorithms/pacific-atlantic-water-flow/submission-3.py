class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = deque(), deque()
        #使用两个True/False来判断是不是可以被flow
        pac = [[False] * cols for _ in range(rows)]
        atl = [[False] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    pacific.append((i,j))
                    pac[i][j] = True
                if (i == rows - 1) or (j == cols - 1):
                    atlantic.append((i,j))
                    atl[i][j] = True
        
        def addWater(i,j,prevheight,ocean,visit):
            if i < 0 or i >= rows or j < 0 or j >= cols or heights[i][j] < prevheight or visit[i][j]:
                return
            
            visit[i][j] = True
            ocean.append((i,j))
            prevheight = heights[i][j]



        while pacific:
            for _ in range(len(pacific)):
                r, c = pacific.popleft()
                addWater(r+1,c,heights[r][c],pacific,pac)
                addWater(r-1,c,heights[r][c],pacific,pac)
                addWater(r,c+1,heights[r][c],pacific,pac)
                addWater(r,c-1,heights[r][c],pacific,pac)
        
        while atlantic:
            for _ in range(len(atlantic)):
                r, c = atlantic.popleft()
                addWater(r+1,c,heights[r][c],atlantic,atl)
                addWater(r-1,c,heights[r][c],atlantic,atl)
                addWater(r,c+1,heights[r][c],atlantic,atl)
                addWater(r,c-1,heights[r][c],atlantic,atl)
        
        for i in range(rows):
            for j in range(cols):
                if pac[i][j] and atl[i][j]:
                    res.append([i,j])
        
        return res
                

        
