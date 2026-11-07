class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        level = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = level
                for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] != -1:
                        q.append((nr,nc))
                        visited.add((nr,nc))
        
            level += 1