class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda t:t[1])
        minheap = [] # [[end,numPass]]
        cap = 0

        for t in trips:
            numPass, start, end = t
            while minheap and start >= minheap[0][0]:
                e, num = heapq.heappop(minheap)
                cap -= num

            else:
                heapq.heappush(minheap,[end, numPass])
            
            cap += numPass
            if cap > capacity:
                return False
                
        return True
