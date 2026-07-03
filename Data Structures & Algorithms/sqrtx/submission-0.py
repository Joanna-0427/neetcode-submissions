class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            res = mid ** 2
            if res == x:
                return mid
            elif res > x:
                right = mid - 1
            elif res < x:
                left = mid + 1
        return right