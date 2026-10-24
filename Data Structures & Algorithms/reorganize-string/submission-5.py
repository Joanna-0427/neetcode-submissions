class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:return ''
        count = Counter(s)
        minheap = [(-v,k) for k, v in count.items()]
        heapq.heapify(minheap)
        res = ''
        q = deque()
        while minheap or q: 
            if not minheap: #空堆，代表目前没有元素可以不相邻
                return ''
            if minheap:
                cnt, k = heapq.heappop(minheap)
                res += k
                if q:
                    t, ele = q.popleft()
                    heapq.heappush(minheap,(t,ele))

                if cnt + 1 < 0:
                    q.append((cnt+1,k))
        
        return res


            

