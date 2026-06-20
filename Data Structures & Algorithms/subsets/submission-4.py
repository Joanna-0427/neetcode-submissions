class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        #dfs负责搜索，不返回值，值保存在res里面
        def dfs(i,path):
            if i >= n:
                res.append(path.copy())
                return
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()

            dfs(i+1,path)
            return res

        dfs(0,[])
        return res
        


        
        




