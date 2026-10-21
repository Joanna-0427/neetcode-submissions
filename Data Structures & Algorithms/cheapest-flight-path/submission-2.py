class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        best = {}
        graph = defaultdict(list)
        minheap = [(0,src,0)]

        for st, des, w in flights:
            graph[st].append((des,w))
        
        while minheap:
            eff, node, stop = heapq.heappop(minheap)
            if node == dst:
                return eff
            
            if stop > k or best.get(node,float('inf')) <= stop:
                continue
            best[node] = stop

            for nb, w in graph[node]:
                heapq.heappush(minheap,(eff+w,nb,stop+1))
        
        return -1
            


