class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def dfs(start):
            #每一层都是一个合法的子集
            res.append(path[:])

            for j in range(start,len(nums)):
                if j > start and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                dfs(j+1)
                path.pop()
                
            
        dfs(0)
        return res

                
            