class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # res = []

        # def dfs(i,path,total):
        #     if i >= len(nums) or total > target:
        #         return 
            
        #     if total == target:
        #         res.append(path.copy())
        #         return

        #     if total < target:
        #         path.append(nums[i])
        #         dfs(i,path,total+nums[i])
        #         path.pop()

        #         dfs(i+1,path,total)

        
        # dfs(0,[],0)
        # return res


        res = []
        n = len(nums)
        nums.sort()
        def dfs(i,sum,path):
            if sum == target:
                res.append(path.copy())
                return
            if sum > target or i >= n:
                return
            if sum < target:
                for i in range(i,n):
                    path.append(nums[i])
                    dfs(i,sum+nums[i],path)
                    path.pop()
              
            return res
        
        dfs(0,0,[])
        return res

































