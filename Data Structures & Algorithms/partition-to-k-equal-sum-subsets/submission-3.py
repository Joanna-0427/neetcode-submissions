class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0: return False
        target = total // k
        edges  = [0] * k
        nums.sort(reverse=True)
        if nums[0] > target:return False

        def dfs(idx,target):
            if idx == len(nums):
                return True
            
            for i in range(k):
                if edges[i] in edges[:i]:
                    continue
                if edges[i] + nums[idx] <= target:
                    edges[i] += nums[idx]
                    if dfs(idx+1,target):return True
                    edges[i] -= nums[idx]
            
            return False
        
        return dfs(0,target)

