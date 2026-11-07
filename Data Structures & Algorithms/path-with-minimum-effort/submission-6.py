class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        minheap = [(0,0,0)]
        maxval = float('-inf')
        visited = set()

        while minheap:
            w,r,c = heapq.heappop(minheap)
            if (r,c) in visited:
                continue
            maxval = max(w,maxval)
            visited.add((r,c))
            if (r,c) == (rows-1,cols-1):
                return maxval
            for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited:
                    eff = abs(heights[nr][nc] - heights[r][c])
                    heapq.heappush(minheap,(eff,nr,nc))
            

                    

                