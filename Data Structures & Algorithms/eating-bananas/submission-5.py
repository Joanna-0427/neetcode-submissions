class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            mid = (l + r) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / mid)
            if t <= h:
                r = mid - 1
                res = mid
            elif t > h:
                l = mid + 1
        return res
            

                
