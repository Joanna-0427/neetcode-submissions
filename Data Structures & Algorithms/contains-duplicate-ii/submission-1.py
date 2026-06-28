class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # l = 0
        # window = set()
        # for r in range(len(nums)):
        #     if r - l > k:
        #         window.remove(nums[l])
        #         l += 1
        #     if nums[r] in window:
        #         return True
            
        #     window.add(nums[r])
        
        # return False
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True
            
            mp[nums[i]] = i
        
        return False
