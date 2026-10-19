class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        
        level = 0
        while q:
            n = len(q)
            for _ in range(n):
                r, c = q.popleft()
                grid[r][c] = level
                for nr, nc in ((0,1),(0,-1),(1,0),(-1,0)):
                    if 0 <= r+nr < rows and 0 <= c+nc < cols and (r+nr,c+nc) not in visited and grid[r+nr][c+nc] != -1:
                        q.append((r+nr,c+nc))
                        visited.add((r+nr,c+nc))
            level += 1
