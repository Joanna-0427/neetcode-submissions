class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])
        
        #每一个pacific，atlantic都向外进行dfs，放入set()，最后取交集
        pacific, atlantic = set(), set()

        def dfs(i,j,prevheight,ocean):
            if i < 0 or i >= rows or j < 0 or j >= cols or (i,j) in ocean or heights[i][j] < prevheight:
                return
            
            ocean.add((i,j))
            prevheight = heights[i][j]
            dfs(i+1,j,prevheight,ocean)
            dfs(i-1,j,prevheight,ocean)
            dfs(i,j+1,prevheight,ocean)
            dfs(i,j-1,prevheight,ocean)


        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    dfs(i,j,0,pacific)
                   
                if (i == rows - 1) or (j == cols - 1):
                    dfs(i,j,0,atlantic)
        
        for r,c in pacific:
            if (r,c) in atlantic:
                res.append([r,c])
        
        return res


        

        
