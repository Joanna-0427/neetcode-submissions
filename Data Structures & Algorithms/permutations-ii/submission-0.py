class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        visited = [False] * len(nums)
        nums.sort()


        def dfs(nums):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            #没有start索引，则每层的值可以从头使用
            for i in range(len(nums)):
                if visited[i]:
                    continue
                #重复值，使用第一个，确保只用一次
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                path.append(nums[i])
                visited[i] = True
                dfs(nums)
                path.pop()
                visited[i] = False
        
        
        dfs(nums)
        return res
            