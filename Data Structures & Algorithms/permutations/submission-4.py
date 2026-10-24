class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        visited = set()

        def dfs(i):
            if len(path) == n:
                res.append(path[:])
                return
            
            for i in range(n):
                if nums[i] in visited:
                    continue
                path.append(nums[i])
                visited.add(nums[i])
                dfs(i+1)
                path.pop()
                visited.remove(nums[i])
        
        dfs(0)
        return res
