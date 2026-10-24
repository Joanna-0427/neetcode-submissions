class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        indexed = sorted(range(n),key=lambda x:(tasks[x][0],tasks[x][1]))
        tasks.sort(key=lambda x:(x[0],x[1]))
        cur = 0
        i = 0
        res = []
        minheap = [] #(processtime,index)
        while i < n:
            if not minheap:
                idx = indexed[i]
                heapq.heappush(minheap,(tasks[i][1],idx))
                cur = tasks[i][0]
                i += 1
                
            while minheap:
                process, idx = heapq.heappop(minheap)
                res.append(idx)
                cur += process

                while i < len(tasks) and tasks[i][0] <= cur:
                    heapq.heappush(minheap,(tasks[i][1],indexed[i]))
                    i += 1
        
        return res
            

