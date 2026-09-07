class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])
        visited = set()
        q = deque()

        def addRoom(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == -1 or (i,j) in visited:
                return
            
            q.append((i,j))
            visited.add((i,j))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist += 1
        



            
            
