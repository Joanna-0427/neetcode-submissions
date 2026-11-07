class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append(((r,c),0)) #2个元素的元组
                    visited.add((r,c))
        

        while q:
            for _ in range(len(q)):
                (r,c), step = q.popleft()
                grid[r][c] = step
                for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] != -1:
                        q.append(((nr,nc),step+1))
                        visited.add((nr,nc))
        
