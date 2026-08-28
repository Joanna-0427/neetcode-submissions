class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        total = 0
        def dfs(i):
            nonlocal total
            if i >= len(nums):
                return
            if total > target:
                return
            
            if total == target:
                res.append(path[:])
                return
            
            path.append(nums[i])
            total += nums[i]
            dfs(i)
            path.pop()
            total -= nums[i]
            dfs(i+1)
        
        dfs(0)
        return res