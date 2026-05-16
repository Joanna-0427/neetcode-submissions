class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quad = []
        res = []
        n = len(nums)
        def dfs(k,start,target):
            if k != 2:
                for i in range(start,n-k+1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    dfs(k-1,i+1,target-nums[i])
                    quad.pop()
                return
            
            l,r = start, n-1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad+[nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
            
        dfs(4,0,target)
        return res
                    
                    












        # nums.sort()
        # res, quad = [], []
        # def dfs(k,start,target):
        #     if k == 2:
        #         left, right = start,len(nums)-1
        #         while left < right:
        #             if nums[left] + nums[right] < target:
        #                 left += 1
        #             elif nums[left] + nums[right] > target:
        #                 right -= 1
        #             else:
        #                 res.append(quad + [nums[left], nums[right]])
        #                 left += 1
        #                 while left < right and nums[left] == nums[left-1]:
        #                     left += 1
        #         return

        #     for i in range(start,len(nums)-k+1):
        #         if i > start and nums[i] == nums[i-1]:
        #             continue
        #         quad.append(nums[i])
        #         dfs(k-1,i+1,target-nums[i])
        #         quad.pop()
                
        # dfs(4,0,target)
        # return res
        


                


