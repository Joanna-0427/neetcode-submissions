class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] == nums[l] == nums[r]:
                l += 1
                r -= 1
            
            #右边有序
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]: #落在有序区间
                    l = mid + 1
                else:
                    r = mid - 1
            
            #左边有序
            else:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1