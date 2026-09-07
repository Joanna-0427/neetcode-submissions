class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        fresh = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                    visited.add((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        
        def addgrid(i,j):
            nonlocal fresh
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0 or (i,j) in visited:
                return
            
            q.append((i,j))
            #或者写成grid[i][j] == 2，原地修改，不用visited;如果不能原地修改，需要visited
            visited.add((i,j))
            fresh -= 1


        times = 0
        #新鲜橘子耗尽的时候就停止，不管q还有没有值；不需要最后一轮的橘子在计算一轮
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                addgrid(r+1,c)
                addgrid(r-1,c)
                addgrid(r,c+1)
                addgrid(r,c-1)
            times += 1
        
        return times if fresh == 0 else -1



