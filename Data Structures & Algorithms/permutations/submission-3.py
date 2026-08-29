class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        visited = set()
        def dfs(nums):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for num in nums:
                if num in visited:
                    continue
                path.append(num)
                visited.add(num)
                dfs(nums)
                visited.remove(num)
                path.pop()
        
        dfs(nums)
        return res

            

        
