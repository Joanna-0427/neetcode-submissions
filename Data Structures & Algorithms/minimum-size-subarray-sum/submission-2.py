class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        total = 0
        minsub = float('inf')

        for j in range(n):
            total += nums[j]

            while total >= target:
                minsub = min(minsub,j-i+1)
                total -= nums[i]
                i += 1
            
        return minsub if minsub != float('inf') else 0
            
            