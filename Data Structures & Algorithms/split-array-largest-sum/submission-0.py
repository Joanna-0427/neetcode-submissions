class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def cansplit(m):
            total = 0
            count = 1
            for n in nums:
                if total + n <= m:
                    total += n
                else:
                    count += 1
                    total = n
            return count <= k
                


        l, r = max(nums), sum(nums)

        minsub = r
        while l <= r:
            mid = (l + r) // 2
            if cansplit(mid):
                minsub = min(mid,minsub)
                r = mid - 1
            else:
                l = mid + 1
        return minsub
        