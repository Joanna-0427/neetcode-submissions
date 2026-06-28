class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')
        window_sum = 0
        l = 0

        for r in range(len(nums)):
            window_sum += nums[r]
            while window_sum >= target:
                minlen = min(r - l + 1,minlen)
                window_sum -= nums[l]
                l += 1
        return minlen if minlen != float('inf') else 0

                
            