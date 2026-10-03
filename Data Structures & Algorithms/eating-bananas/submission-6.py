class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        def total(k):
            total = 0
            for i in range(n):
                if piles[i] > k:
                    t, re = divmod(piles[i],k)
                    if re:
                        t += 1
                    total += t
                elif piles[i] <= k:
                    total += 1
            
            return total


        max_k = max(piles)
        min_k = 1
        l, r = min_k, max_k
        minsub = float('inf')
        
        while l <= r:
            mid = (l + r) // 2
            times = total(mid)
            if times > h:
                l = mid + 1
            else:
                r = mid - 1
                minsub = min(minsub,mid)
        
        return minsub

            

            



