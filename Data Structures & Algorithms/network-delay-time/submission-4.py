class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for start,end,w in times:
            graph[start].append((end,w))
        
        minheap = [(0,k)]
        visited = set()
        ans = 0
        while minheap:
            w,node = heapq.heappop(minheap)
            if node in visited: #弹出时确认最短的已经装入，不在装到visited
                continue
            visited.add(node) #只在pop出来，即确定被选择的时候装入visited
            ans = w
            for ni,weight in graph[node]:
                if ni not in visited: #压入时候优化，已装入visited的节点可以不再压入（共两次确认）
                    heapq.heappush(minheap,(w + weight,ni))
        
        return ans if len(visited) == n else -1


