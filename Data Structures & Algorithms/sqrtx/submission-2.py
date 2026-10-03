class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        idx = -1

        while l <= r:
            mid = (l + r) // 2

            if mid * mid == x:
                return mid
            
            if mid * mid > x:
                r = mid - 1
            
            if mid * mid < x:
                idx = max(mid,idx)
                l = mid + 1
        
        return idx
