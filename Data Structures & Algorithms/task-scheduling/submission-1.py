class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        t = 0
        time = 0
        minheap = []
        q = deque()
        #heap
        for v in count.values():
            heapq.heappush(minheap,(-v))

        while minheap or q:
            time += 1

            if minheap:
                num = heapq.heappop(minheap)
                remain = num + 1

                if remain:
                    q.append((remain,time+n))   #直接用time+n计算目标时间
            
            #需要先判断q是否存在
            if q and q[0][1] == time:
                heapq.heappush(minheap,(q.popleft()[0]))

        return time

        # deque for waiting

        # deque[0] > interval: popleft()
