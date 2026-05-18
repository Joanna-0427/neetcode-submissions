class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)
        # return nums[n//2]

        
        res = 0
        count = 0 
        for i in range(len(nums)):
            if count == 0:
                res = nums[i] 
                count += 1
            if nums[i] == res:
                count += 1
            else:
                count -= 1
        return res

        