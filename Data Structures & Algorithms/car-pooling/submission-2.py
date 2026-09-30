class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        n = len(trips)
        trips.sort(key=lambda x: (x[1],x[2]))
        minheap = []
        total = 0 
        i = 0

        while i < n:
            while minheap and trips[i][1] >= minheap[0][0]:
                end, num = heapq.heappop(minheap)
                total -= num
            
            heapq.heappush(minheap,(trips[i][2],trips[i][0]))
            total += trips[i][0]
            if total > capacity:
                return False
            
            i += 1
            
        
        return True


        