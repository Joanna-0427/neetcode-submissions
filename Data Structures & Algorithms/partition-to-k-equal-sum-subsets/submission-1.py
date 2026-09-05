class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse = True)
        total = sum(nums)
        if total % k:
            return False

        target = total // k
        used = [False] * len(nums)

        def dfs(i,k,subsetsum):
            if k == 0:
                return True

            if subsetsum == target:
                return dfs(0,k-1,0)

            
            for j in range(i,len(nums)):
                if used[j] or subsetsum + nums[j] > target:
                    continue
                
                used[j] = True
                if dfs(j+1,k,subsetsum+nums[j]):
                    return True
                used[j] = False
            
            return False
        
        return dfs(0,k,0)