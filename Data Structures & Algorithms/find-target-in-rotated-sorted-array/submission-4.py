class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = -1
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                if nums[mid] > nums[r] and target > nums[r]:
                    r = mid - 1
                elif nums[mid] > nums[r] and target <= nums[r]:
                    l = mid + 1
                elif nums[mid] <= nums[r]:
                    r = mid - 1
            
            if nums[mid] < target:
                if nums[mid] >= nums[r]:
                    l = mid + 1
                elif nums[mid] < nums[r] and nums[r] >= target:
                    l = mid + 1
                elif nums[mid] < nums[r] and nums[r] < target:
                    r = mid - 1
        
        return -1
                

