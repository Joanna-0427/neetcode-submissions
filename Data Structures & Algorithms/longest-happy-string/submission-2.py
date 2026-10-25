class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        minheap = []
        for i in [(-a,'a'),(-b,'b'),(-c,'c')]:
            if i[0] < 0:
                minheap.append((i[0],i[1]))
        #minheap = [(n, ch)for n, ch in [(-a,'a'),(-b,'b'),(-c,'c')] if n < 0]更简洁的表达
        heapq.heapify(minheap)
        res = []#想表达前两个是不是一样的，直接用res[-2],res[-1]
        while minheap:
            cnt, k = heapq.heappop(minheap)
            if len(res) >= 2 and res[-1] == res[-2] == k:
                if not minheap:
                    break
                cnt2,k2 = heapq.heappop(minheap)
                res.append(k2)
                if cnt2 + 1 < 0:
                    heapq.heappush(minheap,(cnt2+1,k2))
                if cnt + 1 < 0:
                    heapq.heappush(minheap,(cnt,k))
            else:
                res.append(k)
                if cnt + 1 < 0:
                    heapq.heappush(minheap,(cnt+1,k))
        
        return ''.join(res)
            
                




