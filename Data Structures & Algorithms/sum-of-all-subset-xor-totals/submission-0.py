class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i,total):
            if i == len(nums):
                return total
            
            #include
            include = dfs(i+1,total ^ nums[i])

            # not include
            no_include = dfs(i+1,total)

            return include + no_include
        
        return dfs(0,0)
