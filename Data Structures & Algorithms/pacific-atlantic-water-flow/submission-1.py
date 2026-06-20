class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # rows, cols = len(heights), len(heights[0])
        # pac, atl = set(), set()


        # #dfs从一个点开始扩散
        # def dfs(r,c,visit,prevheight):
            
        #     if (r < 0 or r >= rows or c < 0 or c >= cols or 
        #         (r,c) in visit or heights[r][c] < prevheight):
        #         return
        #     visit.add((r,c))
        #     dfs(r + 1, c, visit, heights[r][c])
        #     dfs(r - 1, c, visit, heights[r][c])
        #     dfs(r, c + 1, visit, heights[r][c])
        #     dfs(r, c - 1, visit, heights[r][c])
        
        # #枚举所有起点
        # for r in range(rows):
        #     dfs(r,0,pac,heights[r][0])
        #     dfs(r,cols-1,atl,heights[r][cols-1])
        # for c in range(cols):
        #     dfs(0,c,pac,heights[0][c])
        #     dfs(rows-1,c,atl,heights[rows-1][c])

        # #扫描整个矩阵找交集
        # res = []
        # for r in range(rows):
        #     for c in range(cols):
        #         if (r,c) in pac and (r,c) in atl:
        #             res.append([r,c])
        # return res



        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        def dfs(r,c,visited,preheight):
            if (r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < preheight or (r,c) in visited):
                return

            visited.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                dfs(nr,nc,visited,heights[r][c])
            
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        
        res = []
        for i,j in pac:
            if (i,j) in atl:
                res.append([i,j])
        return res


