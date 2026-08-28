class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #backtracking不断做出选择，探索完后，撤销重来
        #一系列待决策事项适合用[数组]来表示，按某种规则选择/排列，探索到底，再重来

        res = []

        def dfs(i,path):
            if i == len(nums):
                res.append(path[:])
                return
            
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()
            dfs(i+1,path)
        
        dfs(0,[])
        return res

