class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ''
        minheap = []
        for cnt, ch in [(a,'a'),(b,'b'),(c,'c')]:
            if cnt:
                heapq.heappush(minheap,(-cnt, ch))
        
        while minheap:
            cnt, ch = heapq.heappop(minheap)
            if len(res) > 1 and res[-1] == res[-2] == ch:
                if not minheap:
                    break
                cnt2, ch2 = heapq.heappop(minheap)
                res += ch2
                cnt2 += 1
                if cnt2:
                    heapq.heappush(minheap,(cnt2,ch2))
            else:
                res += ch
                cnt += 1
            if cnt:
                heapq.heappush(minheap,(cnt,ch))
        return res
                