class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    visited.add((i,j))
        
        step = 0
        while q:
            for _ in range(len(q)):
                r, c, step = q.popleft()
                #fresh -= 1 #会把本来就是腐烂的橘子，也算一遍
                for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == 1:
                        q.append((nr,nc,step+1))
                        visited.add((nr,nc))
                        fresh -= 1 #这个位置，是表明确认一个新鲜的橘子，被感染，是在减少这个动作发生的那一刻
        
        return step if fresh == 0 else -1

                
