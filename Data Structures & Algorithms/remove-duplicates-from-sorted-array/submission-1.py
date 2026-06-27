class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left,right = 1, 0
        n = len(nums)
        # while right < n:  
        #     nums[left] = nums[right]
        #     while right < n and nums[right] == nums[left]:
        #         right += 1
        #     left += 1
        # return left

        for right in range(1,n):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1
        
        return left



