class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            sumw = mid
            day = 1
            for w in weights:
                if sumw - w < 0:
                    day += 1
                    sumw = mid
                sumw -= w
            
            if day <= days:
                r = mid - 1
                res = mid
            elif day > days:
                l = mid + 1
        return res 
                    
