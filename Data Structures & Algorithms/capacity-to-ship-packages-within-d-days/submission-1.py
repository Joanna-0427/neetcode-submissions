class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # p, re = divmod(sum(weights),days)
        # if re:
        #     p += 1  #p是一个下届，完美能拆分的时候最小值，实际值大于这个
        n = len(weights)
        def times(k):
            total = weights[0]
            times = 1
            for i in range(1,n):
                if total + weights[i] <= k:
                    total += weights[i]
                else:
                    times += 1
                    total = weights[i]
            return times



        l,r = max(weights), sum(weights)
        minsub = float('inf')
        while l <= r:
            mid = (l + r) // 2
            if times(mid) <= days:
                minsub = min(minsub,mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return minsub

            
        