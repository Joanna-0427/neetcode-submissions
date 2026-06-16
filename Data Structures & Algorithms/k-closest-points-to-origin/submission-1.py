class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for i in range(len(points)):
            x, y = points[i]
            dis = (x ** 2) + (y ** 2)
            # minheap.append([dis,(x,y)])
            heapq.heappush(minheap,[-dis,(x,y)])
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        res = [j for i, j in minheap]

            
        # heapq.heapify(minheap)

        # i = 0
        # res = []
        # while i < k:
        #     dis, (x,y) = heapq.heappop(minheap)
        #     i += 1
        #     res.append((x,y))
        
        return res


