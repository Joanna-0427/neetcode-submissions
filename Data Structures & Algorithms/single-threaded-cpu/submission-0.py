class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for index, num in enumerate(tasks):
            num.append(index)
        tasks.sort(key = lambda t: t[0])
        T = tasks[0][0]
        minheap,res = [],[]
    
        i = 0
        while minheap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= T:
                heapq.heappush(minheap,[tasks[i][1],tasks[i][2]])
                i += 1
            
            if minheap:
                protime, id = heapq.heappop(minheap)
                T += protime
                res.append(id)
            else:
                T = tasks[i][0]
        return res
        