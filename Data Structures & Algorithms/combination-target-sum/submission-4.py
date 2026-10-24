class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(idx,total):
            if total == target:
                res.append(path[:])
                return 
            
            if total > target or idx >= len(nums):
                return
            
            path.append(nums[idx])
            dfs(idx,total+nums[idx])
            path.pop()
            dfs(idx+1,total)
        
        dfs(0,0)
        return res