class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        rows, cols = len(heights), len(heights[0])
        
        
        def dfs(i,j,prev_height,data):
            if i < 0 or i >= rows or j < 0 or j >= cols or (i,j) in data or heights[i][j] < prev_height:
                return
            
            data.add((i,j))
            dfs(i+1,j,heights[i][j],data)
            dfs(i-1,j,heights[i][j],data)
            dfs(i,j+1,heights[i][j],data)
            dfs(i,j-1,heights[i][j],data)
        
        res = []
        for i in range(rows):
            dfs(i,0,float('-inf'),pacific)  
            dfs(i,cols-1,float('-inf'),atlantic)
        for j in range(cols):
            dfs(0,j,float('-inf'),pacific)
            dfs(rows-1,j,float('-inf'),atlantic)
        
        for r,c in pacific:
            if (r,c) in atlantic:
                res.append([r,c])
        
        return res




        