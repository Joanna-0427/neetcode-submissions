class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        edges = defaultdict(list)
        t = 0

        for u,v,w in times:
            edges[u].append((w,v))
        
        minheap = [(0,k)]
        while minheap:
            w, node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            t = max(t,w)
            for w1, n1 in edges[node]:
                if n1 not in visited:
                    heapq.heappush(minheap,(w1 + w,n1))
        
        return t if len(visited) == n else -1




