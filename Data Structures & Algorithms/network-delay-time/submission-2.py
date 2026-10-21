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
            if node in visited: #已经访问节点不在装到visited
                continue
            visited.add(node) #只在pop出来，即确定被选择的时候装入visited
            ans = w
            for ni,weight in graph[node]:
                if ni not in visited: #已visited的节点不再压入
                    heapq.heappush(minheap,(w + weight,ni))
        
        return ans if len(visited) == n else -1


