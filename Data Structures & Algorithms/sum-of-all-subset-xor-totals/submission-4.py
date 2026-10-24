class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def dfs(idx,cur):
            nonlocal res
            if idx >= len(nums):
                res += cur
                return
            
            dfs(idx+1, cur)
            dfs(idx+1,cur^nums[idx])
        
        dfs(0,0)
        return res
