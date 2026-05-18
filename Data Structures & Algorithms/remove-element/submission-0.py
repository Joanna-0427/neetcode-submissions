class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '[0,3,2,2,4,3,2,5]'
        n = len(nums)
        write = 0
        right = 0
        while right < n:
            while right < n and nums[right] == val:
                right += 1
            if right < n:
                nums[write] = nums[right]
                right += 1
                write += 1
        return write

            
        