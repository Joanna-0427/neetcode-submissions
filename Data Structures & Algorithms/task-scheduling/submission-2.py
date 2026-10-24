class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        count = Counter(tasks)
        minheap = []
        times = 0
        q = deque()
        for k, val in count.items():
            heapq.heappush(minheap,(-val,k))
        
        while minheap or q:
            times += 1

            if minheap:
                val, k = heapq.heappop(minheap)

                if val + 1 < 0: #如果放在外面就是val，k是之前遗留的值
                    q.append((times+n,val+1,k))
            
            while q and q[0][0] <= times:
                time, cnt, k = q.popleft()
                heapq.heappush(minheap,(cnt,k))
        
        return times


