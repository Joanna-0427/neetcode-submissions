class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            
            #只用nums[mid]，nums[r]两个元素，信息是不够的，不代表这个范围内有断崖，也可能没有断崖
            if nums[mid] > target:
                if nums[mid] == nums[r] == nums[l]:
                    r -= 1
                    l += 1
                elif nums[mid] <= nums[r]:
                    r = mid - 1
                elif nums[mid] > nums[r] and target > nums[r]:
                    r = mid - 1
                elif nums[mid] > nums[r] and target <= nums[r]:
                    l = mid + 1

            if nums[mid] < target:
                if nums[mid] == nums[r] == nums[l]:
                    l += 1
                    r -= 1
                elif nums[mid] <= nums[r] and target > nums[r]:
                    r = mid - 1
                elif nums[mid] < nums[r] and target <= nums[r]:
                    l = mid + 1
                elif nums[mid] > nums[r]:
                    l = mid + 1
        
        return False
                


