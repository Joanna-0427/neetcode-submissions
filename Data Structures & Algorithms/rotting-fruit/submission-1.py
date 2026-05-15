class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        level = 0
        q = deque()
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                
                if grid[i][j] == 2:
                    q.append((i,j))

       
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1
            level += 1
        
        return level if not fresh else -1

                    
                    


            





























        # rows,cols = len(grid),len(grid[0])
        # level = 0
        # fresh = 0
        # directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # q = deque()

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             fresh += 1
        #         if grid[r][c] == 2:
        #             q.append((r,c))

        # while q and fresh > 0:
        #     for _ in range(len(q)):
        #         r,c = q.popleft()
        #         for dr, dc in directions:
        #             nr, nc = r + dr, c + dc
        #             if (nr in range(rows) 
        #                 and nc in range(cols) 
        #                 and grid[nr][nc] == 1):
        #                 grid[nr][nc] = 2
        #                 q.append((nr,nc))
        #                 fresh -= 1
        #     level += 1
            
        # return level if fresh == 0 else -1
                