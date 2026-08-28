class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        #都可以用dfs是因为同样的思想：从当前状态出发，尝试所有的下一步可能，递归到头base case，再把结果往回传；
        #backtracking是一种抽象的树空间，人为定义的逻辑结构，很像tree，也用到dfs相同的思想
        def dfs(i,total):
            if i == len(nums):
                return total
            
            #include
            include = dfs(i+1,total ^ nums[i])

            # not include
            no_include = dfs(i+1,total)

            return include + no_include
        
        return dfs(0,0)
