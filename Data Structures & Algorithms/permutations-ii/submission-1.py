class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        visited = set()
        n = len(nums)

        def dfs():
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if i > 0 and nums[i] == nums[i-1] and i-1 not in visited:
                    continue
                if i in visited:
                    continue
                
                path.append(nums[i])
                visited.add(i)
                dfs()
                path.pop()
                visited.remove(i)
            
        dfs()
        return res            
            