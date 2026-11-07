class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        minheap = [(0,0,src)]
        best = {}

        graph = defaultdict(list)
        for start, end, w in flights:
            graph[start].append((end,w))
        
        while minheap:
            w, stop, node = heapq.heappop(minheap)
            if stop > k+1:
                continue
            if stop > best.get(node,float('inf')):
                continue
            best[node] = stop
            if node == dst:
                return w

            for ni, weight in graph[node]:
                heapq.heappush(minheap,(weight+w,stop+1,ni))

        return -1

            