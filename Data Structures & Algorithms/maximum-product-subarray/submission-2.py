class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min, cur_max = 1, 1
        best = float('-inf')
        n = len(nums)
        for i in range(n):
            cur1 = cur_min * nums[i]
            cur2 = cur_max * nums[i]
            cur_max = max(cur1,cur2,nums[i])
            cur_min = min(cur1,cur2,nums[i])
            best = max(cur_max,cur_min,best)
        
        return best


