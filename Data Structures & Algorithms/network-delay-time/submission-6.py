class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minheap = [(0,k)]
        visited = set()

        graph = defaultdict(list)
        for start, end, weight in times:
            graph[start].append((end,weight))
        
        while minheap:
            w, node = heapq.heappop(minheap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return w
            
            for neigbor, weight in graph[node]:
                if neigbor not in visited:
                    heapq.heappush(minheap,(weight+w,neigbor))
        
        return -1
        


