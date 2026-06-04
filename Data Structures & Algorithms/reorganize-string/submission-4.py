class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        minheap = [[-value,ch] for ch, value in count.items()]
        heapq.heapify(minheap)
        prev = None
        res = ''

        while minheap or prev:
            if prev and not minheap:
                return ''
            
            
            cnt, ch = heapq.heappop(minheap)
            res += ch
            if prev:
                heapq.heappush(minheap,prev)
                prev = None
            if cnt != -1:
                prev = [cnt + 1, ch]
                
        return res
            



