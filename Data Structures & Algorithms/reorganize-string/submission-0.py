class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        minheap = [[-value,ch] for ch, value in count.items()]
        t = 0
        q = deque()
        res = []

        while minheap or q:
            t += 1

            if q and q[0][2] == t:
                heapq.heappush(minheap, q.popleft()[:2])

            if not minheap:
                return ''
            
            if minheap:
                cnt, ch = heapq.heappop(minheap)
                res.append(ch)
                if cnt != -1:
                    q.append([cnt+1, ch, t+2])
        
        return ''.join(res)
            



