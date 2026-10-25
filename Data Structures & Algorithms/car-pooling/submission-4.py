class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:(x[1],x[2]))
        n = len(trips)
        minheap = []
        cap = 0
        i = 0

        while i < n:
            if trips[0][0] > capacity:
                return False
            
            #arrive：
            c, s, t = trips[i]
            while minheap and minheap[0][0] <= s:
                _, cnt = heapq.heappop(minheap)
                cap -= cnt
            
            if cap + c <= capacity:
                heapq.heappush(minheap,(t,c))
                cap += c
            else:
                return False
            i += 1

        return True
            
