class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        minheap = [(0,0,0)]
        visited = set([(0,0)]) #set需要放可迭代对象，元组会把里面元素拆开
        ans = 0
        while minheap:
            eff,r,c = heapq.heappop(minheap)
            visited.add((r,c))
            ans = max(ans,eff)
            if (r,c) == (rows-1, cols-1): #逗号的优先级最低
                return ans
            for nr,nc in ((0,1),(0,-1),(-1,0),(1,0)):
                newr, newc = r + nr, c + nc
                if (newr < 0 or newr >= rows or newc < 0 or newc >= cols) or (newr,newc) in visited: #and比or的优先级高，要用()
                    continue
                effort = abs(heights[newr][newc] - heights[r][c])
                heapq.heappush(minheap,(effort,newr,newc))
        return ans


        
