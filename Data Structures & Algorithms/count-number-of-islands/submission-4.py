class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        def dfs(r,c):
            if (r < 0 or r >= rows or c < 0 or c >= cols 
                or grid[r][c] == '0'):
                return

            grid[r][c] = '0'
            for dr,dc in directions:
                nr, nc = r+dr, c+dc
                dfs(nr,nc)
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i,j)
                    
        
        return islands



            






















        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        # islands = 0
        # directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # # def bfs(r,c):
        # #     q = deque()
        # #     visited.add((r,c))
        # #     q.append((r,c))
        # #     while q:
        # #         r, c = q.popleft()
        # #         directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # #         for dr, dc in directions:
        # #             nr, nc = r + dr, c + dc
        # #             if (nr in range(rows) and nc in range(cols) and grid[nr][nc] == '1' and (nr,nc) not in visited):
        # #                 q.append((nr,nc))
        # #                 visited.add((nr,nc))
                        
                
        # def dfs(r,c):
        #     if (r < 0 or c < 0 or c >= cols or r >= rows or grid[r][c] == '0' or (r,c) in visited):
        #         return
        #     visited.add((r,c))
        #     for dr, dc in directions:
        #         nr,nc = r + dr, c + dc
        #         dfs(nr, nc)
                
            
    
        # if not grid:
        #     return 0
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == '1' and (i,j) not in visited:
        #             dfs(i,j)
        #             islands += 1

        # return islands
            

                