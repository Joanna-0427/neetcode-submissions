class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # prefix = 1
        # for i in range(1,len(nums)):
        #     prefix *= nums[i-1]
        #     res[i] = prefix
        # postfix = 1
        # for i in range(len(nums)-2,-1,-1):
        #     postfix *= nums[i+1]
        #     res[i] *= postfix
        # return res

        prefix = 1
        for i in range(1,len(nums)):
            prefix *= nums[i - 1]
            res[i] = prefix
        
        postfix = 1
        for j in range(len(nums)-2,-1,-1):
            postfix *= nums[j+1]
            res[j] *= postfix
        
        return res



